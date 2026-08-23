# Tech Note: Student Reports

- **Asset ID:** 27709
- **Tech Note #:** 03-25
- **Published:** May 19, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Cha Yang, 4D Inc. Technical Support
- **Page URL:** https://kb.4d.com/assetid=27709
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_21-25_(MAY)/03-25_Student_Reports.hqx

## Overview

Cha Yang demonstrates 4D 2003's new cross-tab reporting mode -- part of the Quick Report editor's new "QR"-prefixed command set that lets developers reproduce programmatically anything the interactive report editor can do -- using a sample database of 23 students, 4 subjects, and 20 exams per subject. The note builds two complete real-world cross-tab reports (a per-class average score, and a weighted final grade) entirely through code, illustrating how relations between Student, Subject, and Exam tables drive which data ends up in the report.

## Key Points

- Sample database: Student, Subject, and Exam tables, related one-to-many (Student→Exam, Subject→Exam), used to build two cross-tab reports.
- Explains relation propagation for reports: a selection in a "One" table restricts the related "Many" table's selection to only the child records of the selected parents, and vice-versa for Many→One; this propagation is effectively a join, so a parent record with no matching children (e.g., a student with no exams in a subject) is silently excluded from the report.
- `RunCrossTab_PerClass` method builds a per-student average score report for a selected subject: queries and relate-many's to the target subject's exams, calls `QR SET REPORT TABLE`/`QR SET REPORT KIND(qr cross report)`, and binds Column 1 = `[Exam]ExamNum`, Column 2 = `[Student]LName+","+[Student]FName` (row titles), Column 3 = `[Exam]Grade` (cell values), each via `QR SET INFO COLUMN`.
- `RunCrossTab_FinalGrade` method computes a weighted final grade across all subjects using `ALL RECORDS([Exam])`, with Column 1 = `[Subject]SubjectName`, Column 2 = student name formula, Column 3 = `[Exam]Grade*[Exam]weight`, then formats the result column as a percentage with `"###.##%"`.
- Aggregation and subtotal behavior at each cell/break level is set with `QR SET TOTALS DATA(area;column;breakLevel;operator)`, e.g. averaging exam scores per student or summing weighted grades per subject.
- Report headers/footers and bold text styling on titles are set with `QR SET HEADER AND FOOTER` and `QR SET TEXT PROPERTY`; output goes to the printer via `QR SET DESTINATION(qr printer)` and `QR RUN`.
- Summarizes the procedure as three repeatable steps: (1) define the parent-table selection, (2) bind columns 1–3 to their data sources, (3) format the cells.

## Featured Technology

- Quick Report Editor cross-tab mode (4D 2003)
- QR SET REPORT TABLE / QR SET REPORT KIND commands
- QR SET INFO COLUMN command
- QR SET TOTALS DATA command
- One-to-many / many-to-one relation propagation into reports
- QR SET HEADER AND FOOTER / QR SET TEXT PROPERTY commands

## Historical Commentary

**Status:** Partially superseded

Cha Yang uses a fictitious student/exam database to demonstrate 4D 2003's brand-new procedural cross-tab reporting commands (the "QR" theme), building two real cross-tab reports -- a per-class average and a weighted final grade -- entirely through code rather than the interactive Quick Report editor. The underlying report engine and QR command set introduced here have been maintained and extended in later 4D versions, so the specific commands shown (QR SET INFO COLUMN, QR SET TOTALS DATA, QR SET REPORT KIND) still exist and work similarly today. That said, for new reporting work most 4D developers today reach first for 4D Write Pro's more modern data-binding and layout capabilities, making this note's classic Quick Report cross-tab approach a still-functional but less commonly chosen technique.

References to newer/updated information:
- The QR command theme shown here (QR SET REPORT TABLE, QR SET INFO COLUMN, QR SET TOTALS DATA, etc.) remains part of current 4D and continues to work as documented
- 4D Write Pro has since become the more commonly used tool for building modern, richly formatted reports, though the classic Quick Report cross-tab engine described here is still available for simpler tabular/grid reporting needs
