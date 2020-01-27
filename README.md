# python_numbers_datatype
# Integers -- Whole Numbers

>Any length allowed up to the memory of the computer
>  - Default in Base 10 (Decimal) --> 	` 0	1	2	3	4	5	6	7	8	9 ` ex--> ` 734 `
>  - Binary (Base 2) --> ` 0  1 ` ex --> ` 0b101101001` 
>  - Octal  (Base 8) `0 1 2 3 4 5 6 7` ex --> `0o4353`
>  - Hexadecimal  (Base 16) `0 1 2 3 4 5 6 7 8 9 A B C D E F` ex --> `0xac4b`

 ## Perform operations on an int
>- operators `+ - * / `
>- special operators 
>	- double division `//` returns the interger of a division
>	- modulus division `%` returns the remainder of a division

>- string to int `int(my_string_number)
>- int to binary `bin(int_number)`
>- int to octal `oct(int_number)`
>- int to hex `hex(int_number)`



# Floating Point -- Any number with a decimal number

>Any division of a number results in a float
>Can be defined using scientific notation (4x10^3 = 4000)

 ## Perform operations on a float
>- division of two ints returns a float
> 	- even if it's a whole number `(4/2 = 2.0)`

>- scientific notation
>- 4e3 == 4x10^3 == 4000.0
>- 4e-3 == 4x10^-3 == 0.004

>- addition of two floating point numbers may result in a error
> - try 0.2 + 0.1 (return 0.3000000000000000004)


# Math and Python Numbers

> - Absolute Value (`abs(-5) == 5`) 
> - Modulus and div (`10 % 3 == 1 -- 10 // 3 == 3`)
> - div and mod (`divmod(10,3) == (3,1)`)
> - maximum (`max([1,2,3,4,5,6,7]) == 7`)
> - minimum (`min([1,2,3,4,5,6,7]) == 1`)
> - power  3^2 (`pow(3,2) == 9 == 3 ** 2`)
> - round to nearest int (`round(3.2) == 3` or `round(3.6) == 4`)
> - sum (`sum[1,2,5,6] == 14`)


## More info on number data types
- [realpython.org -> Strings](https://realpython.com/python-strings/)
- [w3schools.org -> Strings](https://www.w3schools.com/python/python_strings.asp)
- [python.org  -> Strings](https://docs.python.org/3/tutorial/introduction.html#strings)
