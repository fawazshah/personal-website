---
title: Playing around with Rust
slug: rust
publishDate: Feb 2026
description: Thoughts on Rust, coming from C# development.
---

Over the last few months I've been teaching myself Rust. It's a language designed with rock-solid memory safety in mind compared to languages like C++. It features an ownership system and the infamous 'borrow-checker' to eliminate many memory safety bugs at compile time.

I wanted to experiment with it after using [Perspective](https://perspective-dev.github.io/) for a project at work. It's an open-source UI component built for visualising large amounts of streaming data. It was a surprise looking through the code for a UI component to find it was written in Rust!

I've learnt a lot by using the borrow-checker, but my favourite features of the language have actually been completely unrelated to borrow-checking:

- Support for generics in enums. You can define enums that would need a fully-fledged class for equivalent behaviour in C#. An example is the below, which is a very simple implementation of union types:

```rust
enum Either<L, R> {
    Left(L),
    Right(R),
}
```

- The `Result` type. `Result` is a special generic enum that represents the outcome of some operation. It can either be `Ok(T)`, representing success with a return value of type T, or `Err(E)` representing an error of type E. This is a very powerful construct that is used in a lot of internal libraries, for things like I/O and exception handling. For example, to open a file in Rust and handle any errors you can do:

```rust
let file = File::open("file.txt").unwrap_or_else(|err| println!("Failed to open file: {}", err));
```

`File::open` returns a `Result<File>`. `unwrap_or_else` then either returns the successful value out of the `Result`, or calls the given lambda if the Result was an error. This is considerably cleaner than the C# equivalent, which involves more lines of code and an extra level of indentation.

```csharp
try
{
    var stream = File.OpenRead("file.txt");
}
catch (Exception e)
{
    Console.WriteLine($"Failed to open file: {ex.Message}");
}
```

- Perhaps my favourite feature: all variables are immutable by default unless marked with `mut`. This makes debugging so much easier compared to using `var`/`let` in C# or Typescript, where you have to watch out for variables being modified as you step through. This is also enforced at compile time.

```rust
➜  10_references git:(main) ✗ cargo run
   Compiling references v0.1.0 (/Users/fawaz/learning/rust/rust_book/10_references)
error[E0596]: cannot borrow `s` as mutable, as it is not declared as mutable
 --> src/main.rs:3:5
  |
3 |     s.push_str("Modified!");
  |     ^ cannot borrow as mutable
  |
help: consider changing this to be mutable
  |
2 |     let mut s = String::from("Hello, world!");
  |         +++

For more information about this error, try `rustc --explain E0596`.
```

The helpful `rustc --explain` command also gives more details about each error, with examples.

 - Finally, extremely helpful error messages! The Rust compiler will point to the exact line and expression with a mistake. Here, when I reference an undeclared variable, it suggests one with a similar name:

```rust
➜  git:(main) ✗ cargo run
   Compiling references v0.1.0 (/Users/fawaz/learning/rust/rust_book/10_references)
error[E0425]: cannot find value `mystring` in this scope
 --> src/main.rs:4:31
  |
4 |     println!("The length of '{mystring}' is {length}");
  |                               ^^^^^^^^ help: a local variable with a similar name exists: `my_string`
```
 
And here's what it prints when I make the mistake of borrowing a value that has been moved into a function. It highlights the three contributors of the error!

 ```rust
➜  git:(main) ✗ cargo run
   Compiling ownership v0.1.0 (/Users/fawaz/learning/rust/rust_book/9_ownership)
error[E0382]: borrow of moved value: `s`
  --> src/main.rs:6:16
   |
 2 |     let s = String::from("hello");  // s comes into scope
   |         - move occurs because `s` has type `String`, which does not implement the `Copy` trait
 3 |
 4 |     takes_ownership(s);             // s's value moves into the function and so is no longer valid here
   |                     - value moved here
 5 |     
 6 |     println!("{s}");              // this would cause a compile-time error!
   |                ^ value borrowed here after move
   |
```

<br />

It's worth mentioning that aside from the typical compilation targets like `x86_64`, Rust can also be compiled to [WebAssembly](https://webassembly.org/), or `wasm`. This is a low-level instruction format designed to be executable by all major web browsers. Since 2017 it has been supported on Chrome, Firefox, Safari, Opera, and more.

<div style="text-align: center;">
  <img src="/assets/webassembly.png" alt="WebAssembly logo" />
</div>

It's how web components like Perspective can be written in Rust, completely outside the web ecosystem. You can see some examples of data visualised with Perspective [here](https://perspective-dev.github.io/examples/).