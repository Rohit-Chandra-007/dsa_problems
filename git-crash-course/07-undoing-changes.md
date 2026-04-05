# Undoing Changes (Galtiyan Theek Karna)

Git ka sabse bada fayda yeh hai ki aap apni galtiyan aaram se theek kar sakte hain. Aaiye dekhte hain ki alag-alag situations mein kya karna chahiye.

## 1. Uncommitted Changes ko Undo Karna (Working Directory)
Aapne ek file mein changes kiye, par abhi tak `git add` nahi kiya. Aap un changes ko poori tarah discard (delete) karke file ko aakhiri commit wali halat mein lana chahte hain.

```bash
# Naya tarika (Git 2.23+) - Recommended
git restore filename.py

# Purana tarika
git checkout -- filename.py
```

## 2. Staged Changes ko Unstage Karna (Staging Area)
Aapne galti se `git add .` chala diya aur koi galat file "waiting area" mein chali gayi. Aapko use wapas nikalna hai, par uske andar ka code delete nahi karna hai.

```bash
# Naya tarika (Git 2.23+) - Recommended
git restore --staged filename.py

# Purana tarika
git reset HEAD filename.py
```

---

## 3. Commits ko History se Hatana (`git reset`)
Aapne commit kar diya hai, lekin ab aap us commit ko Git history se hi delete karna chahte hain. **Ise sirf apni local branches par use karein, public/shared branches par nahi.**

### A. Safe Undo (`--soft`)
Yeh aapke aakhiri commit ko history se hata dega, **LEKIN aapke changes (code) ko delete nahi karega**. Aapka code staging area mein wapas aa jayega.
```bash
# HEAD~1 ka matlab hai: "Ek commit peechhe jao"
git reset --soft HEAD~1
```

### B. Destructive Undo (`--hard`) - WARNING ⚠️
Yeh history se commit bhi hata dega aur **aapke changes ko bhi poori tarah permanently delete kar dega**. Ise tabhi use karein jab aap sure hon ki aapko wo code bilkul nahi chahiye.
```bash
git reset --hard HEAD~1
```

---

## 4. Public Commits ko Undo Karna (`git revert`)
Agar aapka commit kisi shared branch (jaise `main`) par chala gaya hai jise doosre log use kar rahe hain, toh wahan `git reset` karna sabke liye problem khadi kar dega (kyunki history badal jayegi). Aisi jagah par hum `git revert` use karte hain.

*   **Yeh kya karta hai:** Yeh purane commit ko delete karne ke bajaye, ek bilkul **naya commit** banata hai jo us purane commit ka bilkul ulta (opposite) hota hai. (Jaise "+1" ka revert "-1" hoga).
*   Isse history safe rehti hai, aur galti bhi theek ho jati hai.

```bash
# <commit-hash> ki jagah us commit ki ID dalein jise undo karna hai
git revert <commit-hash>
```
