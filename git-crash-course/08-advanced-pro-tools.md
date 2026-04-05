# Advanced Git Pro-Tools (Life-Savers)

Yeh 4 tools aapko ek average developer se ek "Git Expert" bana denge. Yeh tab kaam aate hain jab aapko code bachana ho, history se khelna ho, ya mushkil bugs dhoondhne hon.

---

## 1. The Ultimate Safety Net (`git reflog`)
Git mein kuch bhi permanently delete nahi hota. `git reflog` aapke har ek action (commit, reset, merge, branch delete) ki ek hidden diary hai jo 30-90 dinon tak save rehti hai.

Agar aapse galti se koi branch ya commit `git reset --hard` se delete ho gaya hai, toh ghabrayein mat:

```bash
# 1. Apni history (log) dekhein
git reflog

# 2. Us list mein us delete hue action ki short ID (jaise HEAD@{2} ya a1b2c3d) dhoondein.
# 3. Phir us state par wapas chale jayein:
git reset --hard <action-id-ya-hash>
```
**Fayda:** Aapka khoya hua code aur commits wapas aa jayenge!

---

## 2. Stashing: Aadhe Adhoore Kaam ko Chupana (`git stash`)
Aap kisi nayi feature par kaam kar rahe hain aur code abhi aadha likha hai (broken hai), isliye aap `commit` nahi kar sakte. Achanak aapko `main` branch mein ek urgent bug fix karna hai. Agar aap bina commit kiye branch switch karenge, toh Git mana kar dega.

**Solution:** Apne aadhe kaam ko ek temporary "daraaz (drawer)" mein daal kar working directory clean kar lein.

```bash
# 1. Apne uncommitted changes ko daraaz mein chhupayein
git stash

# (Ab aap aaram se kisi doosri branch par jakar kaam kar sakte hain)

# 2. Wapas aakar, apne changes ko daraaz se nikal lein aur unhe daraaz se delete kar dein
git stash pop
```
*(Tip: `git stash list` se aap dekh sakte hain ki daraaz mein kya-kya rakha hai).*

---

## 3. Cherry-Picking: Sirf Ek Specific Commit Lana (`git cherry-pick`)
Aapki team ne ek branch mein 10 commits kiye hain. Aapko un 10 mein se sirf 1 commit (jaise "Fixed UI Color") apni `main` branch mein chahiye, baaki 9 nahi. Aap poori branch merge nahi kar sakte.

**Solution:** Aap us ek commit ko chun (cherry-pick) kar apni branch mein laa sakte hain.

```bash
# 1. Pehle us branch par jayein jahan aapko code CHAHIYE (e.g., main)
git switch main

# 2. Phir us specific commit ka hash use karein
git cherry-pick <commit-hash>
```

---

## 4. Bisect: Bug paida karne wale commit ko dhoondhna (`git bisect`)
Sochiye aapka project 1 mahine pehle (v1.0) bilkul theek chal raha tha, par aaj usme ek naya bug hai. Pichle 1 mahine mein 500 commits hue hain aur aapko pata lagana hai ki **kis ek commit ne code break kiya tha**.

**Solution:** `git bisect` ek binary search chalata hai. Yeh in 500 commits ke theek beech (250th) wale par jayega aur aapse puchega, "Kya yahan code theek hai?". Aapke "Haan" ya "Naa" ke basis par yeh jaldi se us "khooni commit" ko dhoondh nikalega.

```bash
# 1. Bisect shuru karein
git bisect start

# 2. Batayein ki current state kharab (bad) hai
git bisect bad

# 3. Batayein ki wo purana commit jahan sab theek tha, wo kaunsa tha (e.g., v1.0 ka hash)
git bisect good <commit-hash-where-it-worked>

# 4. Ab Git aapse puchega. Aapko har baar code run karke check karna hai aur bas yeh likhna hai:
git bisect good   # (Agar us state mein code theek hai)
# YA
git bisect bad    # (Agar wahan bug aa raha hai)

# 5. Jab culprit commit mil jaye toh bisect se bahar aane ke liye:
git bisect reset
```
