# CustomAssemStyleInterpreter

## Documentation
### File structure
For a file to be able to run without errors it must have three main sections, the flags, data and the programs instructions
```
Flags{

}
Data{

}
Program{

}
```
### Flags
Flags can be seperated by commas and will determine certain outputs
| Flag          | Type          | Description                                                       |
| ------------- | ------------- | ----------------------------------------------------------------- |
| Timed         | End           | Will show how long the program took to run at the end             |
| NoExitCode    | End           | Will prevent the program from displaying an exit code at the end  |

### Opcodes

| Opcode        | Syntax                              | Description                                                                                    |
| ------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------- |
| ADD           | ADD <initial & result>, <secondary> | Adds the two numbers stored at the addresses and replaces the data in the first memory address |
