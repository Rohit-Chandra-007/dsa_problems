# Git History & Logs (`git log`)

Jab aap bahut saare commits kar lete hain, toh purane changes dekhne ke liye `git log` ka use hota hai. Har commit ki ek unique ID hoti hai jise **Hash** (SHA-1) kehte hain.

## 1. Basic Log Command
Sabse simple tarika history dekhne ka. Yeh Author, Date, aur Commit Message dikhata hai.
```bash
git log
```
*(Tip: List mein neeche jaane ke liye `Space` aur bahar aane ke liye `q` dabayein).*

## 2. Pro Log Commands (Behtar views ke liye)

### A. One-line Summary
Agar aapko sirf short commit ID aur message dekhna hai (bahut saare commits jaldi dekhne ke liye best hai):
```bash
git log --oneline
```

### B. Graph View
Jab aap branches ke saath kaam karenge (jo hum aage seekhenge), toh yeh command ek visual tree banati hai ki kaunsi branch kahan se nikli aur kahan merge hui:
```bash
git log --graph --oneline --decorate --all
```
*(Tip: Aap is lambi command ka ek chhota alias bhi bana sakte hain apni Git config mein, jaise `git gl` ya `git hist`).*

---

# Git Under the Hood (Plumbing vs Porcelain)

Git internally kaise kaam karta hai, yeh samajhna bahut zaroori hai ek expert banne ke liye.

## 1. Porcelain vs Plumbing Commands
*   **Porcelain (User-friendly):** Yeh wo commands hain jo hum roz use karte hain (jaise `git add`, `git commit`, `git status`). Yeh aasan hoti hain.
*   **Plumbing (Internal):** Yeh wo commands hain jo Git internally data save aur manage karne ke liye use karta hai.

## 2. Git Data Storage: 3 Main Objects
Git aapke code ko simple text files ki tarah save nahi karta. Woh isko objects mein convert karke `.git/objects` folder mein rakhta hai.

1.  **Blob (Binary Large Object):**
    *   Yeh aapki **file ka content** save karta hai.
    *   Isme file ka naam nahi hota, sirf uske andar ka data hota hai.
2.  **Tree:**
    *   Yeh aapke **folder (directory) structure** ko represent karta hai.
    *   Yeh batata hai ki kaunsa 'Blob' kis 'File Name' se juda hua hai.
3.  **Commit:**
    *   Yeh **ek specific 'Tree' ko point karta hai** (yani us waqt ka poora folder structure).
    *   Saath mein yeh Author ka naam, Date, aur Commit Message save karta hai.
    *   Yeh apne se pichle commit (Parent commit) ko bhi point karta hai, jisse history banti hai.

## 3. Magic Command: Internal Data Dekhna (`git cat-file`)
Agar aap kisi commit ya blob ka lamba Hash ID (jaise `f3a2b1...`) jante hain (shuru ke 4-5 characters bhi chalenge), toh aap uske andar ka raw data dekh sakte hain:

```bash
# <hash> ki jagah apni commit ID ya blob ID dalein
git cat-file -p <hash>
```
Yeh aapko Git ka internal magic dikhayega ki usne data kaise save kiya hua hai.
