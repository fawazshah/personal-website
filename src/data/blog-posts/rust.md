---
title: Playing around with Rust
slug: rust
publishDate: Feb 2026
description: Thoughts coming to Rust from mainly C# and Python experience.
---

Over the last few months, out of curiosity, I've been teaching myself Rust. Rust is a language designed with rock-solid memory safety in mind compared to languages like C++. It features an ownership system and the infamous 'borrow-checker' to eliminate many memory safety bugs at compile time.

I wanted to experiment with it after using [Perspective](https://perspective-dev.github.io/), an open-source web component built for visualising large amounts of streaming data. It was a surprise to be looking through the code for a web framework to find it was written in Rust!

Most language newcomers highlight the borrow-checking, but my favourite features of the language (coming from C# and Python) have been these:

 - Extremely helpful error messages. The Rust compiler will point to the exact line and expression with a mistake! Here, when I reference an undeclared variable, it suggests one with a similar name:

```rust
➜  10_references git:(main) ✗ cargo run
   Compiling references v0.1.0 (/Users/fawaz/learning/rust/rust_book/10_references)
error[E0425]: cannot find value `mystring` in this scope
 --> src/main.rs:4:31
  |
4 |     println!("The length of '{mystring}' is {length}");
  |                               ^^^^^^^^ help: a local variable with a similar name exists: `my_string`
```
 
And here's what it prints when I make the mistake of borrowing a value that has been moved into a function. It highlights the three contributors of the error!

 ```rust
 git:(main) ✗ cargo run
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

- Perhaps my favourite feature: all variables are immutable by default unless marked with `mut`. This makes debugging so much easier compared to using `var` or `let` in C#/Typescript where you have to watch out for mutating variables.



Rust is mainly compiled to some version of `x86_64`, depending on your operating system, but one compilation target that has gained popularity is `wasm`, or WebAssembly.

<div style="text-align: center;">
  <img src="/assets/webassembly.png" alt="WebAssembly logo" />
</div>

[WebAssembly](https://webassembly.org/) is a low-level instruction format designed to be executable by all major web browsers. Since 2017 it has been supported on Chrome, Firefox, Safari, Opera, and more.