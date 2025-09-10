// Import necessary namespaces for code analysis, C# syntax parsing, JSON serialization, and file operations
using Microsoft.CodeAnalysis;           // Provides APIs for analyzing .NET code
using Microsoft.CodeAnalysis.CSharp;    // Provides C# specific APIs for code analysis
using Microsoft.CodeAnalysis.CSharp.Syntax; // Provides syntax nodes for C# code
using Newtonsoft.Json;                  // Provides JSON serialization and deserialization
using System;                           // Provides fundamental classes and base classes
using System.IO;                        // Provides classes for input and output operations
using System.Linq;                      // Provides classes and methods for LINQ queries

// Define a class named Program
class Program
{
    // Define the Main method, which is the entry point of the application
    static int Main(string[] args)
    {
        try
        {
            // Check if no command-line arguments are provided
            if (args.Length == 0)
            {
                // Print a JSON error message to the console
                Console.WriteLine(JsonConvert.SerializeObject(new { error = "No file path provided" }));
                return 0; // Return success status code
            }

            // Store the first command-line argument as the file path
            var filePath = args[0];
            // Check if the file does not exist at the provided path
            if (!File.Exists(filePath))
            {
                // Print a JSON error message to the console with file path and current directory
                Console.WriteLine(JsonConvert.SerializeObject(new {
                    error = "File not found",
                    filePath,
                    cwd = Environment.CurrentDirectory
                }));
                return 0; // Return success status code
            }

            // Read the entire content of the file into a string variable
            var code = File.ReadAllText(filePath);
            // Parse the C# code into a syntax tree
            var tree = CSharpSyntaxTree.ParseText(code);
            // Get the root node of the syntax tree as a CompilationUnitSyntax
            var root = tree.GetCompilationUnitRoot();

            // Query to extract class and method information from the syntax tree
            var classes = root.DescendantNodes().OfType<ClassDeclarationSyntax>()
                .Select(cls => new {
                    // Get the name of the class
                    Name = cls.Identifier.Text,
                    // For each class, find all method declarations
                    Methods = cls.Members.OfType<MethodDeclarationSyntax>().Select(m => new {
                        // Get the name of the method
                        Name = m.Identifier.Text,
                        // Get the return type of the method as a string
                        ReturnType = m.ReturnType.ToString(),
                        // Get the parameters of the method
                        Parameters = m.ParameterList.Parameters.Select(p => new {
                            // Get the name of the parameter
                            Name = p.Identifier.Text,
                            // Get the type of the parameter as a string
                            Type = p.Type?.ToString()
                        })
                    })
                });

            // Create an anonymous object with file, usings, namespaces, totals, and class details
            var result = new {
                // Get the file name from the file path
                file = Path.GetFileName(filePath),
                // Get all using directives in the file
                usings = root.Usings.Select(u => u.Name.ToString()),
                // Get all namespace declarations in the file
                namespaces = root.DescendantNodes().OfType<NamespaceDeclarationSyntax>().Select(n => n.Name.ToString()).Distinct(),
                // Calculate total counts of classes and methods
                totals = new {
                    classes = classes.Count(),
                    methods = classes.Sum(c => c.Methods.Count())
                },
                // Store the list of classes with their methods
                classes
            };

            // Serialize the result object to a JSON string without indentation
            Console.WriteLine(JsonConvert.SerializeObject(result, Formatting.None));
            return 0; // Return success status code
        }
        catch (Exception ex)
        {
            // Print a JSON error message to the console in case of an exception
            Console.WriteLine(JsonConvert.SerializeObject(new { error = ex.Message }));
            return 1; // Return error status code
        }
    }
}
