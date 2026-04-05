# Merge Conflicts & Automating Resolution

Jab team mein kaam hota hai, toh sabse bada darr "Merge Conflicts" ka hota hai. Lekin inhe samajhna aur solve karna bahut aasan hai.

## 1. Merge Conflicts Kya Hote Hain?
Git zyada tar code ko khud automatically merge kar leta hai. Lekin conflict tab aata hai jab:
*   Do (2) developers ne ek hi file ki **bilkul same line** par alag-alag code likh diya ho.
*   Ek developer ne file ko delete kar diya ho, jabki doosre ne usme changes kiye hon.

Aisi situation mein Git confuse ho jata hai aur aapse kehta hai ki, *"Main decide nahi kar pa raha, aap khud batao kaunsa code rakhna hai."*

## 2. "Ours" aur "Theirs" (Current vs Incoming)
Jab aap us conflict wali file ko kholenge, toh Git ne wahan kuch markers daal diye honge:

```python
<<<<<<< HEAD (Current Change - Ours)
# Yeh wo code hai jo us branch mein tha jahan aap merge RECEIVE kar rahe hain (e.g., main)
print("Hello from Main branch!")
=======
# Yeh wo code hai jo aap us branch se LAA rahe hain jise aap merge kar rahe hain (e.g., feature)
print("Hello from Feature branch!")
>>>>>>> feature-login (Incoming Change - Theirs)
```

## 3. Conflicts ko Manually Solve Karna
Is conflict ko solve karne ke steps:
1.  Faisla karein ki kaunsa code rakhna hai (Ours, Theirs, ya dono ko milakar naya likhna hai).
2.  Git ke lagaye hue saare markers (`<<<<<<<`, `=======`, `>>>>>>>`) ko delete kar dein.
3.  File ko save karein.
4.  Terminal mein `git add <filename>` chalakar Git ko batayein ki conflict solve ho gaya hai.
5.  Aakhir mein `git commit` chalayein jisse merge poora ho jayega.

*(Note: VS Code jaise editors mein in markers ke upar buttons aate hain jisse yeh kaam sirf ek click mein ho jata hai).*

---

## 4. Automating Conflict Resolution (`rerere`)
**`rerere` = Reuse Recorded Resolution**

Agar aapne ek lamba conflict solve kiya, par kisi wajah se merge ko undo karna pada. Toh agli baar merge karne par wahi same conflict **wapas** aa jayega aur aapko wapas same mehnat karni padegi.

Agar aap `rerere` on kar dete hain, toh Git aapke solve kiye hue conflicts ka solution "yaad" kar leta hai. Agli baar agar bilkul same conflict aaya, toh Git bina aapko pareshan kiye usko **khud hi solve** kar dega!

**`rerere` On karne ki Command (Sirf ek baar karni hoti hai):**
```bash
git config --global rerere.enabled true
```
