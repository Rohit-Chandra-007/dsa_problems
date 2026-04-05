# Git Basics: Repository Setup & File States

Git ko samajhne ka sabse important hissa yeh hai ki files kin-kin stages se hokar guzar ti hain aur code ko "save" kaise kiya jata hai.

## 1. Repository Setup (`git init`)
Kisi bhi naye folder ko Git project banane ke liye us folder mein jaakar yeh command run karein:

```bash
git init
```
**Important:** Yeh command us folder mein ek hidden `.git/` folder bana deti hai. Is folder mein hi aapki saari history save hoti hai. Isko kabhi manually delete na karein.

---

## 2. The 3 States of Git
Git mein aapki files hamesha in 3 mein se kisi ek state mein hoti hain:
1.  **Working Directory (Modified/Untracked):** Aapne file mein code likha hai, par Git ne usko abhi track nahi kiya hai.
2.  **Staging Area (Staged):** Aapne file ko "wait" karwaya hai ki "haan, is file ko main next save mein shamil karna chahta hoon."
3.  **Git Repository (Committed):** Aapka code ab Git history mein permanently save ho chuka hai ek snapshot (photo) ke roop mein.

---

## 3. Everyday Workflow Commands (Sabse zyada use hone wali)

### A. Current Status Check (git status)
Hamesha kisi bhi action se pehle apni repo ki halat check karein:
```bash
git status
```

### B. Files ko Stage karna (git add)
Files ko Working Directory se nikal kar Staging Area (waiting room) mein bhejna:

```bash
# Sirf ek specific file ko add karne ke liye
git add filename.py

# Ek saath saari nayi aur modified files ko add karne ke liye (Sabse common)
git add .
```

### C. Changes ko Commit karna (git commit)
Staging Area mein rakhi hui files ko Git history mein permanent save karna. Hamesha ek clear aur samajh aane wala message dein:

```bash
# -m ka matlab hai "message"
git commit -m "Added two sum solution and tests"
```
