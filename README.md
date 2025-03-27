# LenovoThinkSystemCLI

A Python based rewrite of the Lenovo SMcli tool.

## Introduction

The official Lenovo ThinkSystem CLI tool for the DE2000, DE4000 and DE6000 storage arrays (maybe more) is a little clunky, requires Java, and is not easily scriptable and automatable. A little reverse engineering reveals that it's a simple REST HTTPS API, that can be readily manipulated with the Python requests library.

## Safety & Security

Consider using the "monitor" account, as this has the least privileges.

There are many commands, some perhaps more stateful or multi-step than the ones listed below. Whether these work is an open question.

## Commands

Here are some simple command you can try. Commands appear to be case-insensitive.

```
show storageArray powerInfo
show storageArray batteryAge
```

The full reference is available here: https://pubs.lenovo.com/thinksystem_storage_command_line_interface_11.50.3
