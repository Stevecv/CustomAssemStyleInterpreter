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

| Opcode        | Syntax                              | Description                                                                                          |
| ------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------- |
| ADD           | ADD <initial & result>, <secondary> | Adds the two numbers stored at the addresses and replaces the data in the first memory address       |
| MIN           | MIN <initial & result>, <secondary> | Subtracts the two numbers stored at the addresses and replaces the data in the first memory address  |
| MUL           | MUL <initial & result>, <secondary> | Multiplies the two numbers stored at the addresses and replaces the data in the first memory address |
| DIV           | DIV <initial & result>, <secondary> | Divides the two numbers stored at the addresses and replaces the data in the first memory address    |
| JMP           | JMP <to>                            | Jumps to the instruction at the requested location                                                   |
| IF            | IF <boolean address> <jumpto>       | Jumps to the instruction at the requested location if the data at the requested address is true      |
| EQL           | EQL <data address> <data address>   | Checks if the data at both locations are the same                                                    |
| NOT           | NOT <data address>                  | Will flip a boolean variable at the given location                                                   |
| MOV           | MOV <data address> <to>             | Copies the data from the address requested to the address requested                                  |

Loop that counts to 10:
```
Flags{

}
Data{
	0,
	10,
	true,
	1,
	0,
}
Program{
	PRNT 0;

	MOV 0, 2;
	EQL 2, 1;
	NOT 2;

	ADD 0, 3;
	IF 2, 4;

	END;
}
```
