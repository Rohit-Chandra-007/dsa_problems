# GitHub, Collaboration & Types of Merges

Ab tak humne jo seekha wo aapke computer (local) tak seemit tha. Team mein kaam karne ke liye hume apne code ko internet (jaise GitHub) par dalna padta hai.

## 1. Remotes & GitHub Basics (`git remote`, `push`, `pull`)
Remote ka matlab hai ek aisi repository jo internet (cloud) par host ki gayi hai.

### A. Local ko Cloud se jodna
GitHub par ek khali repo banayein, phir apne terminal mein:
```bash
# 'origin' remote ka standard naam hai. Yeh link ko yaad rakhta hai.
git remote add origin https://github.com/aapka-username/dsa_problems.git

# Check karne ke liye ki remote juda ya nahi:
git remote -v
```

### B. Code Cloud par Bhejna (`git push`)
Aapke local commits ko internet par upload karna:
```bash
# origin = kahan bhejna hai (GitHub)
# main = kaunsi branch bhejni hai
# -u = "upstream" set karta hai taaki agli baar sirf 'git push' likhna pade
git push -u origin main
```

### C. Cloud se Naya Code Lana (`git pull`)
Agar team mein kisi aur ne code change kiya hai, toh use apne computer mein lana:
```bash
git pull origin main
```

---

## 2. Forking & Pull Requests (PR)
Yeh Open-Source projects aur badi companies mein use hone wala workflow hai jahan aapko seedha main code change karne ki permission nahi hoti.

1.  **Fork:** GitHub par kisi original project ki ek exact copy apne account mein banana.
2.  **Clone:** Us copy ko apne computer par download karna.
3.  **Branch & Push:** Nayi branch banakar apne changes karna, aur us branch ko *apne* GitHub repo (fork) par push karna.
4.  **Pull Request (PR):** Original project ke owner ko request bhejna ki, *"Maine yeh feature banaya hai, please isko review karein aur apne main project mein merge kar lein."*

---

## 3. Types of Merges
Jab hum do branches ko jodte hain (merge karte hain), toh Git alag-alag situations ke hisaab se 2 main tarike apnata hai.

### A. Fast-Forward Merge
**Situation:** Aapne `main` se ek branch banayi. Aapne usme kaam kiya. Is beech `main` branch mein kisi ne koi naya kaam *nahi* kiya.
**Kya hota hai:** Git bahut aasani se `main` ke pointer ko aage badha kar aapki branch ke barabar kar deta hai. Yeh sabse clean merge hai. History bilkul seedhi (linear) rehti hai.

### B. 3-Way Merge (Merge Commit)
**Situation:** Aapne `main` se branch banayi aur kaam shuru kiya. Lekin tab tak kisi aur developer ne `main` branch mein naye changes daal diye (push kar diye). Ab dono branches alag-alag disha (direction) mein badh chuki hain.
**Kya hota hai:** Git ab "Fast-Forward" nahi kar sakta. Git aapki branch, current `main` branch, aur us point ko dekhta hai jahan se dono alag hui thi (Common Ancestor). In teeno ko milakar Git ek bilkul naya commit banata hai jise **"Merge Commit"** kehte hain. Yeh history mein branches ka judna dikhata hai.

### C. Rebase (Alternative to Merge Commit)
Bahut saari teams 3-Way Merge ke extra commits pasand nahi karti aur clean history chahti hain. Wo `git merge` ki jagah `git rebase` use karti hain.
**Kya hota hai:** Rebase aapki branch ke commits ko temporarily uthata hai, aapki branch ka starting point (base) `main` branch ke sabse latest commit par shift kar deta hai, aur phir aapke commits uske upar wapas laga deta hai. Isse aap jab bhi merge karenge, wo hamesha "Fast-Forward" hoga.
*(Warning: Rebase sirf apni personal branches par karein, kabhi bhi public/main branch par nahi).*
