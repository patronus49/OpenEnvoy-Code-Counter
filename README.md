# OpenEnvoy-Code-Counter

This repository hosts the assignment solution for OpenEnvoy-Code-Counter. Project is a python based CLI (Command Line Interface) program.

## Project Structure

Project follows a interface pattern with operations files as abstract interfaces and manager classes implementing the interface. 
> Operations: Interface

> Manager: Concrete Class

The modules are defined below,
> Commander - Take the command from terminal and parse the parameters

> Counter - Counter classes implementing various types of syntax counters

> Counter Orchestrator - Project run class executing the command

> Models - Model classes to hold intermediate data and program output data classes

> Test - Test files for counter CLI program

> Utilities - Static utility methods


## Run Commands

Make sure you have python installed on your system,
> Python v3.8

Run the project, with present working directory as project root,
```
> python3.8 main.py --syntax java --comments single-line --counters blank,comments,code,total --input single-file --path default
```
Supported arguments are listed below,
```
--syntax 
	- language of the input code file to be assessed by code counter
	- valid choices: java  
```
```
--comments
	- comments type to be assessed by the coode counter
	- valid choices: single-line
```
```
--counters
	- comma seperated valued for counters employed to assess the input code file
	- valid choices: blank | comments | code |total 
```
```
--input
	- input type of for counter, single file or directory
	- valid choices: single-file  
```
```
--path
	- input file path for the code file to be assessed by code counters
	- valid choices: default | <valid java file path>
```
The test folder contains a sample java test file at path,
> test/java/java_counter_test_file.java
```
import java.util.*;  
  
// file created on 1st Jan 2020  
// author: @openenvoy  
  
public class Main {  
  
    // This is another comment line  
  public static void main(String[] args) {  
        System.out.println("Hello world!"); // code, not comment 11  
  }  
}
```
Running the sample command,
```
> python3.8 main.py --syntax java --comments single-line --counters blank,comments,code,total --input single-file --path default
```
Produces output as,
```
> Arguments =  {'syntax': 'java', 'comments': 'single-line', 'counters': 'blank,comments,code,total', 'input': 'single-file', 'path': 'default'}
> Counter Response =  {
  "blank": 3,
  "comments": 3,
  "code": 6,
  "total": 12
}
```
