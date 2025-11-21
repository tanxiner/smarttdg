# TAMS  
**One‑line purpose**: Centralized registration, TAR management, and notification system with rate limiting.

## Short Overview
TAMS orchestrates user registration, TAR lifecycle, and notification workflows, enforcing business‑defined rate limits and logging all actions.  
It exposes stored procedures for manual data retrieval, SMS alert queuing, and system command execution.  
The system relies on configuration parameters stored in TAMS_Parameters to drive behavior.

## Features
- **Rate‑limited user registration**: Prevents duplicate sign‑ups within configured intervals.  
  Supports: `dbo.sp_TAMS_User_CheckLastUserRegistration`.  
- **Rate‑limited email and SMS notifications**: Controls message frequency based on subject patterns.  
  Supports: `dbo.sp_TAMS_User_CheckLastUserRegistration`, `dbo.sp_TAMS_User_CheckLastUserRegistration`, `dbo.sp_api_send_sms`.  
- **TAR withdrawal**: Users can withdraw a TAR with remarks, updating status and logging the action.  
  Supports: `dbo.sp_TAMS_WithdrawTarByTarID`.  
- **Manual user guide retrieval**: Supplies the current user manual based on effective dates.  
  Supports: `dbo.sp_TAMS_UsersManual`.  
- **Command execution**: Allows execution of arbitrary OS commands via `xp_cmdshell` for administrative tasks.  
  Supports: `dbo.uxp_cmdshell`.  
- **SMS alert queuing**: Enqueues SMS messages for delivery through an external API.  
  Supports: `dbo.sp_api_send_sms`.  

## Primary Workflows
| Workflow | Trigger / Actor | Ordered Steps | One‑line Evidence |
|----------|-----------------|---------------|--------------------|
| **User Registration Check** | User attempts to register | 1. Entry point: request sign‑up. 2. `dbo.sp_TAMS_User_CheckLastUserRegistration` checks @LoginID against last registration and rate limits. 3. If allowed, proceeds to registration (not shown). | `dbo.sp_TAMS_User_CheckLastUserRegistration` |
| **SMS Alert Queuing** | Admin or system initiates an SMS send | 1. Call `dbo.sp_api_send_sms` with contact list, subject, and message. 2. Procedure splits contacts, prepares alert, enqueues via `SMSEAlertQ_EnQueue`. 3. SMS queue receives new alert record. | `dbo.sp_api_send_sms` |
| **TAR Withdrawal** | User initiates a TAR withdrawal | 1. Trigger: request to withdraw a TAR. 2. `dbo.sp_TAMS_WithdrawTarByTarID` verifies current status. 3. Updates `TAMS_TAR` with new status, remark, UID. 4. Writes audit entry to `TAMS_Action_Log`. | `dbo.sp_TAMS_WithdrawTarByTarID` |
| **Command Execution** | System administrator issues a command | 1. Call `dbo.uxp_cmdshell` with @cmd. 2. Inside, `xp_cmdshell` executes the OS command. | `dbo.uxp_cmdshell` |
| **User Manual Retrieval** | Request for current user manual | 1. Call `dbo.sp_TAMS_UsersManual`. 2. Reads `TAMS_Parameters` for `UManual` within effective dates. 3. Returns manual content. | `dbo.sp_TAMS_UsersManual` |

## Key Data Domains and Artifacts
- **TAMS_Registration** – Holds user sign‑up records, registration dates, and status flags.  
- **TAMS_User** – Stores UID, name, and contact details for each system user.  
- **TAMS_TAR** – Captures technical assistance requests, their line, status, and remarks.  
- **TAMS_WFStatus** – Contains workflow status definitions for TARs.  
- **TAMS_Action_Log** – Audit log recording every status change or administrative action.  
- **TAMS_Parameters** – Central configuration store (rate limits, user manual content, effective/expiry dates).  
- **SMSEAlertQ (procedure)** – Queueing mechanism referenced by `dbo.sp_api_send_sms` (alert records reside in a log or queue table not explicitly listed).  

*Heavy‑use tables*: `TAMS_Registration` and `TAMS_Parameters`.  
No explicit staging or temporary table patterns are apparent in the current design.