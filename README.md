# Job Application Email Automation

A Python script to automatically send job application emails to multiple HR contacts with a personalized message and resume attachment.  
Supports multiple recipients, error handling, and logging. Built for professional use and easy GitHub sharing.

---

## Overview

This Python script automates sending job application emails to multiple HR contacts. It allows you to send personalized emails with your resume attached, saving time when applying to multiple job openings.  
The script uses **SMTP with Gmail** and the **EmailMessage** module to send emails securely.

---

## Features

- Send a single email to one or multiple HR email addresses.  
- Customize email subject and body.  
- Attach your resume in PDF format.  
- Automatically handles sending through Gmail SMTP with SSL encryption.  
- Prints confirmation messages for each email sent.  

---

## Prerequisites

Before running the script, ensure you have:

1. Python 3.7 or higher installed.  
2. Gmail account credentials (email and **App Password** if 2FA is enabled).  
3. Your resume in PDF format, placed in the same folder as the script.  
4. Basic Python packages installed (built-in `smtplib` and `email`).  

---

