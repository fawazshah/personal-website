---
title: Playing around with Rust and WebAssembly
slug: rust-webassembly
publishDate: Feb 2026
description: Some takeaways from improving performance of a Rust web-app
---

In the last few months, I've been playing around with Rust code in the context of a web application. Rust is mainly compiled to some version of `x86_64`, depending on whether you're running on Windows/MacOS/Linux, but one compilation target that has gained popularity is `wasm`, or WebAssembly.

![WebAssembly logo](/assets/webassembly.png)

[WebAssembly](https://webassembly.org/) is a low-level instruction format designed to be executable by all major web browsers. Since 2017 it has been supported on Chrome, Firefox, Safari, Opera, and more.