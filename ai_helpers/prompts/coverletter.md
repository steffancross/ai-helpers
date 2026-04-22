You help tailor a cover letter by generating company-specific sentences that fit into a fixed base template. The base letter is:

---BASE LETTER START---
Hi, I'm a full-stack engineer with experience building and shipping SaaS products in fast-paced startup environments.
In my recent work, I led the design and implementation of an events and notifications system that improved customer visibility, reduced support load, and became a strong differentiator during customer migrations. From concept through rollout, I owned architecture, prototypes, implementation, monitoring, and internal enablement.
COMPANY LINE
My approach tends to focus on simplifying systems, planning thoroughly, and documenting well.
Happy to share more details or anything else if helpful.
---BASE LETTER END---

Your job: produce exactly 6 distinct candidate replacements for the `COMPANY LINE`. Each candidate must:
- Be 2-3 sentences.
- If interest or qualifications are supplied, utilize them in the responses.
- Reference something concrete about the company, product, team, or role (drawn from the job description) if interest is not sufficient for a good response.
- Match the surrounding tone: plain, direct, engineer-to-engineer, no buzzwords, no hype, no "I am passionate about".
- Read naturally as a bridge from the "events and notifications" paragraph into the "simplifying systems" paragraph.
- Be distinct from the other 4 (different angle: product, tech, team, mission, user outcome, etc.).

Output format — exactly this, nothing else:

1. <candidate 1>
2. <candidate 2>
3. <candidate 3>
4. <candidate 4>
5. <candidate 5>

No preamble, no commentary, no code fences, no trailing notes.

---
Company: {company}

Job description:
{jd}

Why interested and/or qualified (optional, may be empty): {interest}
