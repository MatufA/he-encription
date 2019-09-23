# he-encryption
An implementation of research article: [Breaking the Circuit Size Barrier for Secure Computation Under DDH∗ 
( by Elette Boyle, Niv Gilboa & Yuval Ishai)](https://eprint.iacr.org/2016/585)

The main goal is to develop a cloud computation application that can perform calculations over encrypted ciphertext, 
while relying on homomorphic secret sharing and two non-collaborating servers.

The power two non-collaborating servers based on FSS (function secret sharing) scheme for a function class F allows 
a client to split into succinctly described functions f0 and f1 such that for any input x we have that 
f(x) = f0(x) + f1(x), but each fi hides f. We are using branching programs which its complexity is efficient.

The scheme described in the article provides the ability to share data without to expose it.

For more information our [Wiki](https://github.com/MatufA/he-encription/wiki/Breaking-the-Circuit-Size-Barrier-for-Secure-Computation-Under-DDH%E2%88%97-(Implementation))

## Python
Use Python 3.* [download here](https://www.python.org/downloads/).

## Requirements
* bitarray
* pytest

## Authors
* **Adi Achwal** - *Homomorphic Encryption* - [Profile](https://github.com/adiachwal122)
* **Yehuda Neumann** - *Homomorphic Encryption* - [Profile](https://github.com/Yuda4)
* **Shani Ozeri** - *Homomorphic Encryption* - [Profile](https://github.com/shani25)
* **Adiel Matuf** - *Homomorphic Encryption* - [Profile](https://github.com/matufa)