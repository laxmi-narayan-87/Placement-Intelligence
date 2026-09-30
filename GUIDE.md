# Placement Intelligence — User Guide

## What is Placement Intelligence?

Placement Intelligence is a personal hiring-research workflow for a 2027 B.Tech CSE / AI-ML fresher in India. It reduces the need to manually check company career pages, job boards, assessment platforms, college placement notices, and hiring announcements.

It focuses on fresh software and technology hiring, fresher and internship opportunities, campus/off-campus hiring, deadlines, assessments, interviews, eligibility, locations, application-status verification, and changes to previously reported opportunities.

## How to use it in ChatGPT

If Placement Intelligence is installed/enabled in your ChatGPT environment, start with a natural request that asks for placement intelligence.

Recommended starter:

> Give me today's placement updates using Placement Intelligence. Prioritize fresh, verified, actionable India software/technology hiring information for my profile.

You can then ask follow-up questions in the same conversation.

### Common prompts

> Find new software engineering jobs for me today.

> What's new since yesterday?

> Show only jobs whose application deadline is still open.

> Check today's campus placement updates.

> Find new off-campus SDE, Python, backend, QA, SDET and AI/ML opportunities.

> Show assessment and coding-test updates for this week.

> Check whether the application for Company X is still live.

> Verify this job post against the official company career page.

> Find opportunities suitable for a 2027 CSE/AI-ML fresher.

## Main use cases

### 1. Daily placement briefing

> Give me today's placement updates using Placement Intelligence. Show only high-signal opportunities and prioritize deadlines, assessments, and newly opened applications.

Expected sections include immediate actions, new opportunities, campus updates, off-campus opportunities, assessments, upcoming deadlines, changes, and concrete next actions.

### 2. Find new jobs

> Find new software/technology jobs for 2027 CSE/AI-ML freshers in India from the last 3 days. Verify that the applications are currently open.

Useful roles include Software Engineer/SDE, Software Developer, Backend Developer, Python Developer, QA Engineer, SDET, Automation Testing, AI/ML Engineer, AI Engineer, GenAI, Agentic AI, Data/ML, and relevant internships.

### 3. Track deadlines

> Show all active placement opportunities with upcoming deadlines. Sort them strictly by deadline and verify application status.

### 4. Verify an application

> Verify whether this job application is currently live. Check the official company career page and tell me whether I can still apply.

Status should be distinguished as Confirmed, Reported, or Unverified rather than guessed.

### 5. Campus placement intelligence

> Give me the latest campus placement updates relevant to a 2027 CSE/AI-ML student.

Prioritize official college placement communications and include company, role, eligibility, package, registration deadline, assessment date, interview date, and instructions when available.

### 6. Off-campus hiring

> Find the latest off-campus software hiring opportunities in India for 2027 freshers. Verify the application links and exclude closed applications.

### 7. Assessment and OA tracking

> Show upcoming coding tests, OAs, aptitude tests, hiring challenges and technical interviews relevant to my profile.

Track assessment platform, date/time, duration, topics, eligibility, registration deadline, and official instructions when available.

### 8. Company-specific tracking

> Check current fresher and internship hiring at [Company]. Focus on India and verify every application from the official source.

### 9. Objective comparison

> Compare these opportunities based on eligibility, role, location, deadline, CTC/stipend, assessment process and application status.

The workflow should present factual differences rather than subjective rankings.

### 10. Final verification before applying

> Before I apply, verify this opportunity for eligibility, graduation year, experience, location, deadline, application status and official application URL.

## Recommended daily workflow

1. Morning discovery: Ask for today's placement updates.
2. Filter: Ask for opportunities that objectively match your profile.
3. Verify: Check important application status using official sources.
4. Act: Review deadlines and upcoming assessments.
5. Apply: Open the official application page and submit the application yourself.
6. Evening change check: Ask, What's new since this morning?

## Verification behavior

Source priority:
1. Official company career page
2. Official application or assessment portal
3. College/university placement notice
4. Reputable job platform
5. Reliable secondary placement source
6. Public social/community source

For important opportunities, check role, graduation year, experience, location, deadline, CTC/stipend, assessment date, interview date, application status, and official application URL where available.

If something cannot be verified, explicitly say so. Never invent salary, CTC, stipend, deadline, eligibility, job ID, assessment date, hiring status, or application URL.

## Status labels

**Confirmed** — supported by an authoritative source or independently corroborated.

**Reported** — published by a secondary source but not independently confirmed.

**Unverified** — a claim was found, but there is insufficient evidence to confirm it.

**Open** — the application is accepting applications based on available evidence.

**Closed** — the application is no longer accepting applications or the deadline has passed.

## Profile configuration

The default profile is designed around 2027 graduation, B.Tech CSE / AI & ML, fresher / 0–1 year experience, India, and software/backend/Python/QA/SDET/automation/AI/ML roles.

You can customize it:

> Update my placement profile to prioritize backend development and Python roles.

> Add Mumbai and Pune to my preferred locations.

> Include remote India internships.

> Focus more on SDET and automation testing roles.

> Exclude roles requiring more than one year of experience.

## Prompt templates

**Daily:** Give me today's placement updates using Placement Intelligence.

**Recent:** Find software hiring updates from the last 3 days.

**Weekly:** Give me the most important placement updates from the last 7 days.

**Deadline:** Show only active applications with upcoming deadlines.

**New:** What's new since yesterday?

**Campus:** Show the latest campus placement updates relevant to my profile.

**Off-campus:** Find new off-campus software jobs for 2027 freshers.

**Assessments:** Show upcoming OAs, coding tests and hiring challenges.

**Verification:** Verify whether this job is still open.

**Company:** Track current fresher hiring at [Company].

**Eligibility:** Check whether I am objectively eligible for these roles.

**Application status:** Check whether these application forms are still live.

## Important limitations

Placement Intelligence is a research workflow. It fetches fresh information when invoked; it is not an always-running crawler by itself.

It should not invent job details, treat old reposts as new jobs, claim an application is live without evidence, fabricate deadlines or assessment dates, or produce subjective company rankings.

For recurring daily delivery or conditional alerts, use ChatGPT automation separately.

## Recommended first message

> Give me today's placement updates using Placement Intelligence. Prioritize fresh, verified, actionable India software/technology hiring information for a 2027 B.Tech CSE/AI-ML fresher. Check whether each important application is actually live, prioritize official sources, include deadlines and upcoming assessments, and avoid duplicate or stale posts.