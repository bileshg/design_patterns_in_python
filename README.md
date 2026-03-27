# Design Patterns in Python

Small study repository for working through and documenting design patterns in Python.

The codebase is organized as a set of focused examples under `src/`, starting with SOLID principles and then moving through creational, structural, and behavioral patterns. The goal is not to be a framework or polished library, but a readable place to experiment, refactor, and keep notes while studying.

## What is in the repo

- SOLID principle examples
- Creational patterns such as Builder, Factory, Prototype, and Singleton
- Structural patterns such as Adapter, Bridge, Composite, Decorator, Facade, Flyweight, and Proxy
- Behavioral patterns such as Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, and Visitor

## Layout

Most material lives in numbered section folders inside `src/`, for example:

- `sec01-solid`
- `sec02-builder`
- `sec03-factories`
- ...
- `sec23-visitor`

Within each section, examples are further split by topic and kept intentionally small so they can be run or modified independently.

## Running examples

This repository is mainly for local exploration. In most cases, you can run an example module directly from the project root with Python after activating the virtual environment and adjusting the target path to the file you want to inspect.

## Note on origin

This repo was forked and then reorganized for personal study. The underlying example material is adapted from work originally contributed by Dmitri Nesteruk, with local changes for structure, cleanup, and experimentation.
