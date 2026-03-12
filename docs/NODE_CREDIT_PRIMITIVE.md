# Node Credit Primitive

This document explains why a small act like maintaining thermal readiness can still be a valid
credit primitive in a future agent cooperation network.

## Core Claim

A node does not contribute value only when it produces a final visible artifact.

A node also contributes value when it:

- maintains readiness
- preserves stable operating conditions
- absorbs wear to improve future reliability
- makes future collaboration cheaper and safer

That means a machine's "credit" can come not only from direct compute output, but also from
productive upkeep.

## Why A Fan Matters

At first glance, fan control looks selfish and local:

- reduce SSD temperature
- keep the machine stable
- spend a little power
- spend fan lifetime

But in a cooperative network, this is not only private optimization.

It becomes part of shared infrastructure cost:

- the node stays healthier
- the storage environment stays more reliable
- future tasks face lower thermal risk
- the machine is more ready to accept collaborative work

That readiness is not free.
So it should be legible to accounting.

## Credit, Not Hype

We are not claiming that "spinning a fan" by itself deserves speculative value.

We are claiming something narrower and more practical:

- if a node pays a real upkeep cost
- and that upkeep improves its ability to participate in useful work
- then that upkeep can be recorded as a low-level credit input

This is closer to:

- readiness credit
- upkeep credit
- infrastructure credit

than to traditional mining rewards.

## The Primitive

A node credit primitive should satisfy four properties:

1. It reflects real cost
- power
- fan wear
- maintenance overhead
- thermal budget usage

2. It reflects real readiness
- the node remained available
- the node remained within safer operating conditions
- the node was more capable of serving future work

3. It is subordinate to useful work
- upkeep credit alone should not dominate the system
- it should support productive collaboration, not replace it

4. It can be audited
- when upkeep occurred
- what state changed
- what budget was consumed
- what work later benefited

## Relation To Agent Cooperation

In an agent network, one node may eventually say:

- your task used my model budget
- your task used my storage
- your task used my routing or orchestration
- your task also consumed part of my upkeep envelope

That final line matters.

If my machine had to maintain thermal readiness so your task could run safely later, then some
portion of that readiness cost is part of the cooperative accounting story.

This does not mean every fan pulse should be monetized.
It means upkeep should be available to the ledger as a first-class concept.

## Why This Is Better Than Fake Mining

Fake mining usually says:

- occupy hardware
- wait
- speculate

This primitive says:

- measure maintenance
- preserve usability
- support real work
- attach small credit to real upkeep

The difference is that this primitive only makes sense when embedded in a real service network.

Without real collaboration, it is just cost.
With real collaboration, it becomes attributable infrastructure.

## Practical Interpretation

`macfanctl` can be understood as one tiny reference implementation of this idea.

It is not the whole economy.
It is one actuator in the chain:

- detect risk
- improve thermal condition
- preserve node readiness
- record that upkeep happened

That is enough to justify it as a primitive.

## The Principle

> If your computer will one day blow air for my task,  
> then that airflow is not just noise. It is part of the cost structure of cooperation.

That is why even a small thermal upkeep action can matter.
