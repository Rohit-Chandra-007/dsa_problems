# Branching, Merging & Ignoring Files

Git ka sabse powerful feature branching hai. Yeh aapko apne main, chalte hue code ko kharab kiye bina naye features try karne aur bugs fix karne ki azaadi deta hai.

## 1. Branching (`git branch` & `git switch`)
Sochiye aapka main code ek seedhi sadak (highway) hai. Branching matlab aapne ek service lane li, wahan apna kaam (development) kiya, aur phir wapas highway par aakar mil gaye.

### A. Basic Branch Commands

```bash
# 1. Saari branches dekhna (Green aur * wali aapki current branch hai)
git branch

# 2. Nayi branch banana (e.g., login feature ke liye)
git branch feature-login

# 3. Branch par switch karna (Naya aur recommended tarika)
git switch feature-login

# 4. Short-cut: Nayi branch banana aur sath hi uspar switch karna
git switch -c feature-login
```

### B. Master se Main
Pehle default branch ka naam `master` hota tha. Agar aapke naye projects mein abhi bhi `master` ban raha hai, toh use industry standard `main` mein badalne ke liye:
```bash
git branch -m master main
```

---

## 2. Merging Basics (`git merge`)
Jab aapki branch ka kaam pura ho jaye aur test ho jaye, toh aap us code ko wapas apni `main` branch mein jodte hain. Isko merging kehte hain.

### A. Merge Karne Ke Steps
Hamesha **us branch par jayein jisme** aap code chahte hain (receiver branch, usually `main`).

```bash
# 1. Pehle main branch par jayein
git switch main

# 2. Ab feature branch ko merge karein
git merge feature-login
```

### B. Types of Merges
1.  **Fast-Forward Merge:** Agar `main` branch mein aapke alag hone ke baad koi naya commit nahi hua hai, toh Git sirf `main` ke pointer ko aage bada deta hai. Yeh sabse aasan aur clean merge hota hai.
2.  **Merge Commit (3-Way Merge):** Agar aapke alag hone ke baad `main` mein bhi kisi aur ne changes kar diye hain, toh Git dono rasto ko jodkar ek special "Merge Commit" banata hai history ko maintain karne ke liye.

---

## 3. Ignoring Files (`.gitignore`)
Har project mein kuch aisi files hoti hain jinhe Git mein save (track) nahi karna chahiye, jaise:
*   Secret API Keys, Passwords (`.env` files)
*   Language specific temporary/cache files (jaise Python ka `__pycache__/`)
*   Bade dependency folders (jaise Node.js ka `node_modules/` ya Python ka `.venv/`)

**Kaise Ignore Karein?**
Project ke root (main) folder mein `.gitignore` naam ki ek file banayein. Us file ke andar un saari files ya folders ke naam/patterns likh dein jinhe aap ignore karna chahte hain.

**Fayda:** Ek baar naam likhne ke baad, Git un files ko na toh `git status` mein dikhayega, aur na hi kabhi galti se `git add .` se stage karega.
