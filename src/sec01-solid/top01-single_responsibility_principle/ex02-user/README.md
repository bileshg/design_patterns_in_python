## Note on the Design

While the design in `prg03-srp_violation.py` clearly violates the Single Responsibility Principle (SRP), this example uses several distinct classes to properly create, store, and contact users of a platform. This separation of concerns neatly illustrates the SRP.

However, this design is not without its flaws. For example, the `SenderInterface` is closely coupled with the `User` class to extract the necessary recipient information when sending a message. Despite this, the design serves its purpose in demonstrating the SRP, which is the main goal of this example.
