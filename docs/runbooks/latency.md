# Runbook: slow responses and timeouts

For the alerts BalanceLatencyHigh, ReminderFeeLatencyHigh, CpuSaturation and GatewayTimeouts on sample-app.

sample-app runs one worker process behind the proxy. When one endpoint keeps that worker busy, every other endpoint queues behind it, and the proxy answers 504 after 30 seconds. Each action below has an id; say which one you took in the incident channel.

## RB-LAT-1: Check for a release just before the onset
Kind: check
Rule: deploys
Risk: none
Look for a release deployed in the 30 minutes before the first alert, and whether it changed the code in the failing requests' stacks. A release that did is the first suspect; one that changed other files is not.

## RB-LAT-2: Roll back the release
Kind: rollback
Risk: medium
Applies when: a release deployed shortly before the onset changed code in the failing stacks.
Ask the release approver to roll the target back to the release before it. The platform allows a rollback only to a release the target ran before, and records it.

## RB-LAT-3: Shed load on the slow endpoint
Kind: mitigate
Risk: low
Applies when: one endpoint takes most of the worker's time and the others queue behind it.
Rate-limit the slow endpoint at the proxy (start at 5 requests a second per client) so the other endpoints answer again. Tell the endpoint's users. Remove the limit once the cause is fixed.

## RB-LAT-4: Add a worker process
Kind: mitigate
Risk: low
Applies when: the worker is busy but CPU is not saturated.
Start sample-app with one more worker process. With CPU already saturated this only adds queueing: shed load first.

## RB-LAT-5: Ask for a load test of the slow endpoint
Kind: follow_up
Risk: none
Run the Performance agent's load test on the target (the `performance` flow) to find where the endpoint's time goes in the code, and open a story for the fix.

## RB-LAT-6: Check earlier incidents
Kind: check
Rule: incidents
Risk: none
Look for earlier incidents about the same endpoint or code; a known cause or workaround saves time.

## RB-LAT-7: Page the owning team
Kind: escalate
Risk: none
Applies when: the cause is outside sample-app (the proxy, the database, the network).
Page the team that owns the failing dependency, with the timeline so far.
