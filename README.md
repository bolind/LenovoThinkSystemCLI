# LenovoThinkSystemCLI

A Python based rewrite of the Lenovo SMcli tool.

## Introduction

The official Lenovo ThinkSystem CLI tool for the DE2000, DE4000 and DE6000 storage arrays (maybe more) is a little clunky, requires Java, and is not easily scriptable and automatable. A little reverse engineering reveals that it's a simple REST HTTPS API, that can be readily manipulated with the Python requests library.

## Commands

Here are some simple command you can try. Commands appear to be case-insensitive.

```
show storageArray powerInfo
show storageArray batteryAge
```

The full reference is available here: https://pubs.lenovo.com/thinksystem_storage_command_line_interface_11.50.3/97C3A6EC-568A-45A6-B632-75959A5A2BA3_