# Basic Search Demo

A very simple demo of how search engines may work, written in Python. 

Note it is therefore impractical, inefficient and not robust, due to its purpose and my ability. 

## What's this?

When I was seeking for information about how search engines work, I came across an answer on Quora (["How can you build a basic search engine on your own? - Jayesh Lalwani's answer - Quora"](https://qr.ae/pNv9VX)). I appreciated it as such a clear and informative demonstration that I decided I could immediately build one demo following the instructions, and here it is. 

## What does this program do?

It first picks up the data from "raw_data.txt" from the same directory, makes an inverted index accordingly and then asks for user input. 

All inputs (including data and user input) are treated as lowercase ones. There are simple synonym-replacement, stopword-removal and result-sorting functions, but little work is actually done inside them. NTLK is not introduced, for the purpose of  keeping it simple (and for I'm lazy :P). 

```
Please type in what you want to search: Pizza
Italian Pizza
- http://yummypizza.com
Sicilian Pizza
- http://yummierpizza.com

Please type in what you want to search: i want pizza
Italian Pizza
- http://yummypizza.com
Sicilian Pizza
- http://yummierpizza.com

Please type in what you want to search: Italian Pizza
Italian Pizza
- http://yummypizza.com
Italian Shoes
- http://sexyshoes.com
Sicilian Pizza
- http://yummierpizza.com

Please type in what you want to search: italy pizza  
Italian Pizza
- http://yummypizza.com
Italian Shoes
- http://sexyshoes.com
Sicilian Pizza
- http://yummierpizza.com

Please type in what you want to search: shoes
Italian Shoes
- http://sexyshoes.com

Please type in what you want to search:
```