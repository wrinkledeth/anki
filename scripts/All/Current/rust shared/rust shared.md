

## What expression prints a given string value to the console?

<div class="code">println!(string)</div>

## What serves as the standard entry point for all Rust programs?

The <div class="code">main</div> function.

## What keyword precedes the declaration of a variable?

<div class="code">let</div>

## Why would the following code refuse to compile?<div><br></div><div class="code">let x = 5;<br>x += x % 2;</div>

Variables are immutable by default. Reassignments to the current version of <div class="code">x</div> are not allowed.

## What keyword can be used within a variable declaration to override its default immutability?

<div class="code">mut</div>

## What is the identifier of Rust's standard library?

<div class="code">std</div>

## Why is there a <div class="code">!</div> in the expression <div class="code">println!()</div>?

<div class="code">println!</div> is a macro, not a function.

## What expression creates and returns a new instance of a <div class="code">String</div>?

<div class="code">String::new()</div>

## What module of <div class="code">std</div> is responsible for handling input and output?

<div class="code">io</div>

## What method of <div class="code">std::io</div> is responsible for reading a line of console input?

<div class="code">stdin().read_line(&amp;output)</div>

## What symbol proceeds a keyword when indicating a reference (a pointer)?

<div class="code">&amp;</div>

## What is a tuple?

A primitive fixed-length type that can group multiple values of different types together in an indexed list.

## What is an array?

A primitive fixed-length type that can group multiple values of the same type together in an indexed list.

## What's the primary difference between tuples and arrays?

Tuples can store values of different types, arrays cannot.

## What type stores an unsigned 8-bit integer?

<div class="code">u8</div>

## What type stores a signed 8-bit integer?

<div class="code">i8</div>

## What type stores a signed 32-bit value?

<div class="code">i32</div>

## What type stores an unsigned 32-bit value?

<div class="code">u32</div>

## What are the four scalar types of Rust?

Integers<div>Floating-point numbers</div><div>Booleans</div><div>Characters</div>

## What binary encoding format are signed integers stored in?

Two's complement.

## When assigning a variable's type implicitly, what is Rust's default integer type?

<div class="code">i32</div>

## What data type stores 64-bit floating-point numbers?

<div class="code">f64</div>

## How can a variable's type be assigned explicitly during declaration?

By following the variable's identifier with a colon, followed by the desired type.<div><br></div><div>Example:</div><div class="code">let y: f32 = 2.17;</div>

## What are the five basic mathematical operators of Rust?

<div class="code">+</div> (Addition)<div><div class="code">-</div> (Subtraction)</div><div><div class="code">*</div> (Multiplication)</div><div><div class="code">/</div> (Division)</div><div><div class="code">%</div> (Remainder)</div>

## What one-byte type represents one of two possible states?

<div class="code">bool</div>

## What is Rust's most primitive alphabetic type, which is used to store singular character values?

<div class="code">char</div>

## How is a string literal declared?

By surrounding text with double quotes. (<div class="code">"</div>)<div><br></div><div>Example:</div><div class="code">"This is a string"</div>

## How is a <div class="code">char</div> value declared?

By surrounding a character with single quotes. (<div class="code">'</div>)<div><br></div><div>Example:</div><div class="code">'G'</div>

## What encoding standard does Rust use for <div class="code">char</div> and <div class="code">String</div>?

UTF-8

## How are elements of tuples accessed?

By following the tuple's identifier by a period, then the index to access.<div><br></div><div>Example:</div><div class="code">let element = tup.2;</div><div><br></div><div><div class="code">element</div> will be assigned the 3rd element in <div class="code">tup</div>.</div>

## How is a tuple declared?

By surrounding a comma-separated list of values in parentheses.<div><br></div><div>Example:</div><div class="code">let tup = (1, 2, 3, 4);</div>

## How is an array declared?

By surrounding a comma-separated list of values in square brackets.<div><br></div><div>Example:</div><div class="code">let arr = [1, 2, 3, 4];</div>

## How can a tuple/array be destructured into multiple individual variables?

By assigning a tuple-like collection of identifiers to a tuple/array of equal length.<div><br></div><div>Example:</div><div class="code"><div>let tup = (54, 4.1, 's');</div><div>let (an_int, a_float, a_char) = tup;</div></div><div><br></div><div><div class="code">an_int</div>, <div class="code">a_float</div>, and <div class="code">a_char</div> will be assigned their respective values according to the order of values in <div class="code">tup</div>.</div>

## How do you explicitly declare an array with a certain number of elements of a given type?

By following the array's identifier with a colon, followed by its contained type, then a semicolon, then its size, all contained within square brackets.<div><br></div><div>Example:</div><div class="code">let arr: [i32; 5] = [1, 2, 3, 4, 5]</div><div><br></div><div>This explicitly states that the array contains five 32-bit integer values.</div>

## How can an array with a given number of duplicated elements be initialized without any repetition?

By beginning the array's body with the element to duplicate, followed by a semicolon, then the number of duplications.<div><br></div><div>Example:</div><div class="code">let screaming = ['A'; 5]</div><div><br></div><div><div class="code">screaming</div> will be initialized to <div class="code">['A', 'A', 'A', 'A', 'A']</div>.</div>

## How are elements of an array accessed?

By following the array's identifier with the index to be accessed in square brackets.<div><br></div><div>Example:</div><div class="code">let element = arr[5];</div><div><br></div><div><div class="code">element</div> will be assigned the 6th value of <div class="code">arr</div>.</div>

## What data type are arrays exclusively indexed by?

<div class="code">usize</div>

## What keyword initiates the beginning of a function declaration?

<div class="code">fn</div>

## How are function parameters formatted?

<div class="code">fn function_name(param_1: type, ... param_n: type) {}</div>

## What method of strings removes all leading and trailing whitespace from the string?

<div class="code">trim()</div>

## Why wouldn't the following code compile?<div><br></div><div class="code"><div>fn some_function(cool_parameter, lame_parameter) {</div><div>&nbsp; ...assume there's valid code in here...</div><div>}</div></div>

Parameter types must be specified in a function's declaration.

## In Rust, what is the difference between a statement and an expression?

An expression returns some value after being executed, a statement does not.

## Why won't the following code compile?<div><br></div><div class="code">let x = let y = 0;</div>

The <div class="code">let</div> statement doesn't return a value.

## How can a new scope be created within another scope?

By encompassing some code in curly braces.<div><br></div><div>Example:</div><div class="code"><div>let y = {</div><div>&nbsp; let x = 3;</div><div>&nbsp; x + 1</div><div>};</div></div><div><br></div><div><div class="code">y</div> will be assigned a value of <div class="code">4</div>.</div>

## How are blocks, made with curly braces, instructed to return the value of a given expression?

By terminating the block with the desired expression, and omitting that expression's semicolon.<div><br></div><div>Example:</div><div class="code"><div>let distance_squared = {</div><div>&nbsp; delta_x = x1 - x2;</div><div>&nbsp; delta_y = y1 - y2;</div><div>&nbsp; delta_x * delta_x + delta_y * delta_y</div><div>};</div></div><div><br></div><div><div class="code">distance_squared</div> will be assigned the result of the last expression in the block.</div>

## What will a block return if its last expression ends with a semicolon?

<div class="code">()</div><div>An empty tuple.</div>

## What does terminating an expression with a semicolon turn the expression into?

A statement.

## How does a function indicate the type of value it returns, if any?

<div>By following the parameter parentheses group with a thin arrow, followed by the intended return type.</div><div><br></div>Example:<div class="code">fn how_many_birds() -&gt; u128 { ... }</div>

## How is a value returned from a function?

By using the <div class="code">return</div> keyword, or by terminating the function with the expression to return without a semicolon.

## How are comments formatted?

By preceding any text with <div class="code">//</div>.

## How is an if-else expression formatted?

<div class="code">if condition {<div>&nbsp; ...code to run if condition is true...</div><div>} else {</div><div>&nbsp; ...code to run if condition is false...</div><div>}</div></div>

## Why won't the following code compile?<div><br></div><div class="code"><div>let condition = 0;</div><div>if condition {</div><div>&nbsp; println!("The condition is true.");</div><div>} else {</div><div>&nbsp; println!("The condition is false.");</div><div>}</div></div>

Nothing is implicitly converted to <div class="code">bool</div> when used in condition statements.

## How can subsequent conditions be checked in an if expression until a checked condition is true?

By using else-if expressions.

## How is the most basic loop expression formatted?

<div class="code">loop {<div>&nbsp; ...code to repeat until escaped...</div><div>}</div></div>

## What keyword escapes a loop and stops it from repeating again?

<div class="code">break</div>

## How can a value be returned from a loop expression?

By following the <div class="code">break</div> keyword with the expression to evaluate and return.<div><br></div><div class="code"><div>let mut counter = 0;</div><div>let one_million = loop {</div><div>&nbsp; counter += 1;</div><div><br></div><div>&nbsp; if counter == 1000000 {</div><div>&nbsp; &nbsp; break counter;</div><div>&nbsp; }</div><div>}</div></div><div><br></div><div><div class="code">one_million</div> will be assigned a value of <div class="code">1000000</div>.</div>

## How is the <div class="code">while</div> loop expression formatted?

<div class="code">while condition {<div>&nbsp; ...code to repeat until condition is false...</div><div>}</div></div>

## How can a <div class="code">for</div> loop be used to iterate over every element in an iterable type?

<div class="code">for element in array_name.iter() {<div>&nbsp; ...code to operate on each instance of element...<br><div>}</div></div></div>

## What's the primary difference between string literals and the <div class="code">String</div> type?

String literals are immutable and stored on the stack, whereas <div class="code">String</div> types are mutable and stored in the heap.

## What method of <div class="code">String</div> types adds a string literal to the <div class="code">String</div>?

<div class="code">push_str(string_to_add)</div>

## Why won't the following code compile?<div><br></div><div class="code"><div>let greeting = String::from("Aloha");</div><div>let salutation = greeting;</div><div><br></div><div>println!("{}", greeting);</div><div>println!("{}", salutation);<br></div></div>

Only one variable can own a reference at once, so the <div class="code">String</div> that <div class="code">greeting</div> first referenced was moved to <div class="code">salutation</div>.

## What method creates a deep copy of some data stored on the heap and returns its reference?

<div class="code">clone()</div>

## What does it mean if a type has the <div class="code">Copy</div> trait?

The type is stored only on the stack, and will be copied to any variables that attempt to bind to their value.<div><br></div><div class="code"><div>Example:</div><div>let x = 5;</div><div>let y = x;</div><div>println!("{}, {}", x, y);</div></div><div><br></div><div>Unlike with types like <div class="code">String</div>, this is valid because the value of <div class="code">x</div> is copied to <div class="code">y</div>, rather than <div class="code">y</div> being given a reference to the value pointed to by <div class="code">x</div>.</div>

## In what case are tuples stored exclusively on the stack, meaning they have the <div class="code">Copy</div> trait?

When the contents of the tuple all have the <div class="code">Copy</div> trait.

## Why won't the following code compile?<div><br></div><div class="code"><div>let dark_secrets = String::from("My diary");</div><div><br></div><div>whisper(dark_secrets);</div><div><br></div><div>println!("{}", dark_secrets);</div></div>

The reference to <div class="code">dark_secrets</div> is moved to the function body of <div class="code">whisper</div>, where it falls out of scope once the function ends. This leaves <div class="code">dark_secrets</div> without anything to point to.

## How can a variable be passed into a function without that function taking ownership of it?

By passing in the variable's reference using <div class="code">&amp;</div><div class="code">.</div><div class="code"><br></div>(Also known as immutable reference)

## How can a function accept a reference to one of its parameters, instead of the parameter itself?

By prefixing the parameter's type with <div class="code">&amp;</div>.<div><br></div><div>Example:</div><div class="code"><div>fn calculate_length(text: &amp;String) -&gt; usize {</div><div>&nbsp; text.len()</div><div>}</div></div><div><br></div><div><div class="code">text</div> will be assigned a reference to the actual value of the given <div class="code">String</div>, rather than its actual contents.</div>

## How can a function be passed a reference that allows for the editing of the referenced value?

By passing the reference into the function with the <div class="code">mut</div> keyword.<div><br></div><div>Example:</div><div class="code"><div>mysterious_function(&amp;mut david);</div></div><div><br></div><div><div class="code">mysterious_function</div> will be given a mutable reference of <div class="code">david</div>, meaning that all changes made to <div class="code">david</div> in the function body will affect the original variable itself.</div>

## Why won't the following code compile?<div><br></div><div class="code"><div>let mut s = String::from("hello");</div><div>let r1 = &amp;mut s;</div><div>let r2 = &amp;mut s;</div><div>println!("{}, {}", r1, r2);</div></div>

Only one mutable reference to a piece of data is allowed at a time.

## Why won't the following code compile?<div><br></div><div class="code"><div>let mut s = String::from("hello");</div><div>let r1 = &amp;s;</div><div>let r2 = &amp;s;</div><div>let r3 = &amp;mut s;</div></div>

No mutable references to any particular piece of data are allowed when an immutable reference to the same data still exists.

## Why won't the following code compile?<div><br></div><div class="code"><div>fn main() {</div><div>&nbsp; let home_address = demolish_home();</div><div>}</div><div><br></div><div>fn demolish_home() -&gt; &amp;String {</div><div>&nbsp; let home = String::from("Home");</div><div>&nbsp; &amp;home</div><div>}</div></div>

<div class="code">home</div> falls out of scope at the end of <div class="code">demolish_home</div>. The returned reference value would dangle, and the compiler will not allow references to data that no longer exists.

## What method of <div class="code">String</div> types converts the value into an array of bytes?

<div class="code">as_bytes()</div>

## What data type does <div class="code">enumerate</div> return?

<div class="code">tuple</div>

## How is a byte literal formatted?

By following <div class="code">b</div> with the byte character to specify.<div><br></div><div>Example:</div><div><div class="code">b' '</div> refers the the byte code of a space character.</div>

## How is a string slice formatted?

<div class="code">&amp;string_name[start_index..end_index]</div>

## What type is used when referring to string slices?

<div class="code">&amp;str</div>

## Why won't the following code compile?<div><br></div><div class="code"><div>let mut hello_word = String::from("hello word");</div><div>let hello = &amp;hello_word[..5];</div><div>hello_word.clear();</div><div>println!("the first word is: {}", hello);</div></div>

Calling <div class="code">clear</div> would attempt to alter <div class="code">hello_world</div>, which would not be allowed due to the current immutable reference owned by <div class="code">hello</div>.

## What type are string literals?

<div class="code">&amp;str</div><div><br></div><div>They are in fact references to slices of bytes directly on the stack, which is also why they're immutable.</div>

## How can a <div class="code">String</div> be easily converted into a string literal?

<div>By taking an entire slice of the <div class="code">String</div>.</div><div><br></div><div>Example:</div><div class="code">&amp;string_name[..]</div>

## What data type would the following expression return?<div><br></div><div class="code"><div>let array = [1, 2, 3, 4];</div><div>let slice = &amp;array[2..]</div></div>

<div class="code">&amp;[i32]</div>

## What is a struct?

A collection of related values.

## How is a struct declared?

<div class="code">struct Struct_name {<div>&nbsp; field_1: type,</div><div>&nbsp; field_2: type,</div><div>&nbsp; ...</div><div>&nbsp; field_n: type,</div><div>}</div></div>

## How is a new instance of a struct initialized?

By following the name of the struct with curly braced which contain the key-value pairs of all the struct's fields.<div><br></div><div>Example:</div><div class="code"><div>let user1 = User {</div><div>&nbsp; email: String::from("someone@example.com"),</div><div>&nbsp; username: String::from("someusername123"),</div><div>&nbsp; active: true,</div><div>&nbsp; sign_in_count: 1,</div><div>};<br></div></div><br>This creates a new instance of a <div class="code">User</div> struct and assigns it to <div class="code">user1</div>.

## How can the struct update syntax be used to initialize a new instance of a struct that shares values with another given instance of the struct?

By specifying the fields to initialize separately, then following them with two periods and the name of the instance to take values from.<div><br></div><div>Example:</div><div class="code"><div>let user2 = User {</div><div>&nbsp; email: String::from("another@example.com"),</div><div>&nbsp; username: String::from("anotherusername567"),</div><div>&nbsp; ..user1</div><div>};</div></div><div><br></div><div>This will initialize <div class="code">user2</div> to the given values, then leave the rest of the parameters up to whatever values <div class="code">user1</div> contains.</div>

## How are tuple structs declared?

<div class="code">struct Struct_name(type_1, type_2, ... type_n);</div>

## What is the main difference between structs and tuple structs?

Tuple structs don't have names associated with their fields, and are accessed with integer indexes like tuples.

## What string formatting placeholder is used for debug printing?

<div class="code">{:?}</div>

## What string formatting placeholder is used for debug printing with added formatting?

<div class="code">{:#?}</div>

## How are methods of a struct declared?

<div class="code">impl Struct_name {<div>&nbsp; fn method_name(&amp;self) -&gt; type {</div><div>&nbsp; &nbsp; ...</div><div>&nbsp; }</div><div>}</div></div><div><br></div><div>As many methods may be declared in an <div class="code">impl</div> block as desired. Extra parameters beyond <div class="code">self</div> may be added with normal syntax.</div>

## How is an associated function of a struct defined?

Similar to a method of a struct, just without the <div class="code">self</div> parameter in the function declaration.<div><br></div><div>Example:<br><div class="code">impl Struct_name {<div>&nbsp; fn function_name(parameter: type, ...) -&gt; return_type {</div><div>&nbsp; &nbsp; ...</div><div>&nbsp; }</div><div>}</div></div></div>

## How are associated functions called?

By following the type's name with two colons, then the function's name.<div><br></div><div>Example:</div><div class="code">String::new()</div>

## How is an enum declared?

<div class="code">enum Enum_name {<div>&nbsp; enum_1,</div><div>&nbsp; enum_2,</div><div>&nbsp; ...</div><div>&nbsp; enum_n,</div><div>}</div></div>

## How are values of an enum addressed?

By following the name of the enum with two colons, then the value of the enum to use.<div><br></div><div>Example:</div><div class="code">Color::Blue</div>

## How can enum values be declared to contain associated values?

<div class="code">enum Enum_name {<div>&nbsp; enum_1(type_1, type_2, ... type_n),</div><div>}</div></div>

## How are methods of enums declared?

In exactly the same way as methods of structs.

## What is Rust's alternative to the null type that most programming languages have?

The <div class="code">Option</div> enum, which can either be <div class="code">Some(T)</div> or <div class="code">None</div>.

## How is the <div class="code">match</div> expression formatted?

<div class="code">match variable_name {<div>&nbsp; value =&gt; some_code(),</div><div>&nbsp; ...</div><div>}</div></div>

## How is a function that is capable of returning <div class="code">None</div> declared?

By using <div class="code">Option&lt;T&gt;</div> as the return type, replacing <div class="code">T</div> with the appropriate type.<div><br></div><div class="code"><div>Example:</div><div>fn divide(x: i32, y: i32) -&gt; Option&lt;f64&gt; {</div><div>&nbsp; if y == 0 {</div><div>&nbsp; &nbsp; return None;</div><div>&nbsp; }</div><div>&nbsp; Some(x / y)</div><div>}</div></div><div><br></div><div><div class="code">divide</div> will return <div class="code">Option&lt;f64&gt;</div> for any case in which <div class="code">y</div> is not <div class="code">0</div>. Otherwise it will return <div class="code">None</div>, due to the undefined nature of the operation.</div>

## How are values contained within an <div class="code">Option</div> handled?

By processing them with a <div class="code">match</div> expression.

## Why won't the following code compile?<div><br></div><div class="code"><div>fn plus_one(x: Option&lt;i32&gt;) -&gt; Option&lt;i32&gt; {</div><div>&nbsp; match x {</div><div>&nbsp; &nbsp; Some(i) =&gt; Some(i + 1),</div><div>&nbsp; }</div><div>}<br></div></div>

Not all cases of <div class="code">Option</div> were handled.

## How can all values of a given type be specified in a <div class="code">match</div> expression?

By using the <div class="code">_</div> placeholder.<div><br></div><div>Example:</div><div class="code"><div>let score = 0u8;</div><div>match score {</div><div>&nbsp; 1 =&gt; println!("One"),</div><div>&nbsp; 3 =&gt; println!("Three"),</div><div>&nbsp; _ =&gt; println!("Not one or three"),</div><div>}</div></div>

## How can a <div class="code">match</div> expression be instructed to do nothing on matching a certain value?

By putting <div class="code">()</div>, the unit value, in place of any code that would otherwise be run.

## What variable naming scheme is preferred in Rust?

snake_case

## What method of iterators converts the iterator into a given collection type of the iterator's data?

<div class="code">collect()</div>

## What must be provided to the <div class="code">collect()</div> method in order to specify what type the data should be collected into?

Either a type hint for the variable being declared, or use of Rust's turbofish operator on the method call.<div><br></div><div>Example:</div><div class="code"><div>let text = string::from("this is some text");</div><div>let words = text.split(" ").collect::&lt;Vec&lt;&amp;str&gt;&gt;();</div><div>let words: Vec&lt;str&amp;&gt; = text.collect();</div></div><div><br></div><div>The two last lines produce the same effect.</div>

## What method of strings separates the string into an iterator of string slices according to a given delimiter?

<div class="code">split(delimiter)</div>

## What string formatting expression converts a number to its representation in binary?

<div class="code">{:b}</div>

## How can a program's command line arguments be referenced?

<div class="code">std::env::args()</div>

## What method of <div class="code">Result</div> types can be used to concisely only allow for <div class="code">Ok</div> values, and panic upon encountering <div class="code">Err</div>?

<div class="code">expect("Error message")</div>