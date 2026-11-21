# POS Report to PR

A small Python demo for handing a cashier's bug report to Devin. The sample POS app closes a shift successfully but produces no receipt when a custom closeout template is missing. The starter includes the bug so Devin has something to reproduce and fix.

## Reproduce the bug

Requires Python 3.9 or newer. Uses the standard library.

```sh
git clone https://github.com/bayubmtr/pos-report-to-pr.git
cd pos-report-to-pr
python3 demo_pos.py
python3 bridge.py preview report.json
```

The POS command prints `{"status": "closed", "receipt": null}`. The preview prints the exact request body the bridge would send. Both commands run locally without credentials.

## Hand off to Devin

Connect this GitHub repo to a Devin organization with permission to open a branch and a pull request. Set `DEVIN_ORG_ID` and `DEVIN_API_KEY` locally for a credential with the `UseDevinSessions` permission.

```sh
python3 bridge.py submit report.json
python3 bridge.py status SESSION_ID
```

`submit` starts a session and prints its ID and URL. The session prompt asks Devin to reproduce the bug, demonstrate a failing and passing regression test, and open a draft PR. `status` prints any PR URLs reported by the session.

The CLI takes a JSON report with `message`, `context`, and `expected`. The Poke integration would fill those fields from the conversation and send the resulting link back. This prototype uses the sample JSON file for that handoff. The live Devin session and PR flow still need a connected workspace to verify.

[Devin API documentation for creating a session](https://docs.devin.ai/api-reference/v3/sessions/post-organizations-sessions) · [Reading session status](https://docs.devin.ai/api-reference/v3/sessions/get-organizations-session)
