# Git Configuration (git config)

Git ko batana zaroori hai ki aap kaun hain taaki aapke commits (changes) track ho sakein. 

## 1. Global Setup (Poore system ke liye)
Yeh commands aapke poore computer par default naam aur email set kar dengi:

```bash
# Apna naam set karne ke liye
git config --global user.name "Aapka Naam"

# Apna email set karne ke liye
git config --global user.email "aapka.email@example.com"
```

## 2. Local Setup (Sirf ek specific project ke liye)
Agar aap kisi specific project (jaise office project) ke liye alag email use karna chahte hain, toh us project ke folder mein jaakar yeh run karein (bina `--global` ke):

```bash
git config user.name "Aapka Naam"
git config user.email "office.email@example.com"
```

## 3. Configuration Check Karna
Yeh check karne ke liye ki aapne kya set kiya hai:

```bash
# Global config dekhne ke liye
git config --global --list

# Current project ka config dekhne ke liye
git config --list
```
