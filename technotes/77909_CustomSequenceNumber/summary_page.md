# Tech Note 17-23: Custom Sequence Number

**Author:** Kristopher Merolla, Technical Services Engineer, 4D Inc.
**Published:** December 20, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77909
**Download:** https://kb.4d.com/DLTN/TN/2017/17-23_CustomSequenceNumber.zip

## Proposition
Builds a custom, concurrency-safe sequence-number generator for 4D using semaphores and transaction suspension, as a robust alternative to relying solely on 4D's standard auto-increment or built-in Sequence number function.

## Key Points
- **Motivation:** many applications (invoicing, logging) need a guaranteed, gap-free, ordered sequence number across simultaneous users, which standard auto-increment primary keys don't always cleanly provide.
- **Built-in Sequence number function reviewed:** the note explains its inputs/outputs as a baseline before presenting the custom alternative.
- **Semaphores as the concurrency primitive:** explained via a real-world analogy, then applied to guard the critical section where the next sequence value is computed and reserved.
- **Dedicated sequenceNumber table:** stores the current sequence state, isolated from the business data tables.
- **Sample multi-table test structure:** Table_X tables and _run/_runTableX/createRecord test methods simulate concurrent record creation to validate correctness.
- **Transaction suspension:** used alongside semaphores to ensure the sequence-number reservation and the eventual record save are handled correctly without collisions.
- **End-to-end flow:** getNextSequenceNumber's output flows into createRecord and is saved as the record's sequence number field.

## Featured Technology
- Semaphores
- Transactions (transaction suspension)
- Built-in Sequence number function (as point of comparison)
- Auto-increment / primary keys

## Best Practices Highlighted
1. Use a semaphore to guard the critical section of sequence-number generation to prevent race conditions between concurrent users.
2. Use transaction suspension appropriately so partially-completed sequence reservations don't leak or double-allocate a number.
3. Isolate sequence-generation state in a dedicated table rather than embedding it ad hoc in business tables.

## Context / Positioning
This note addresses a classic multi-user database concurrency problem using core, foundational 4D primitives (semaphores, transactions) that predate and are orthogonal to later architectural shifts like ORDA or Project Mode — it's a "timeless" 4D concurrency-control technique rather than a feature tied to a specific 4D release era.

## Historical Commentary
**Status:** Still relevant

Semaphores and transaction control (including transaction suspension) remain current, fully supported 4D language features, and the concurrency problem this note solves — safe, gap-free sequence generation with multiple simultaneous users — is unaffected by 4D's later Design-Mode-to-Project-Mode or ORDA transitions. This technique is just as applicable whether records are ultimately created via classic 4D commands or via ORDA's `new()`/`save()`.

If anything has changed, it's mostly stylistic (e.g., typed `var` declarations now available instead of classic C_LONGINT/C_TEXT-style declarations), but the core semaphore-plus-transaction pattern documented here remains a recommended, still-taught approach for building reliable custom sequence numbers in 4D today.
