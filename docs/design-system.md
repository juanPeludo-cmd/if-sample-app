# sample-app design system

UI for sample-app is built only from the components in `design-system/components.json`
(package `@sample/design-system`), styled only with the tokens in `design-system/tokens.json`.

- Layout: `Panel` (a titled card, tone neutral, warning or danger) and `Stack` (vertical or
  horizontal, gap from the `space` tokens).
- Content: `Text`, `KeyValue`, `Badge`, and `Money` for every amount (EUR, two places, as
  ADR-0002 keeps money), with its own `label`. A binding is plain (`{invoice.total}`): the
  component formats the value, so a binding never carries a filter or a format.
- Actions: `Button`, whose `action` names an operation of the API contract by its
  operationId, so every action the UI offers exists in the contract.

No raw colours, sizes or fonts: a value that is not a token is a design-system departure.
