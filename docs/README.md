# Requirements

- Have UV installed,
  if you don't have UV, you'll have to run:
  ```sh
  python -m venv .venv
  source .venv/bin/activate
  pip install .
  ```
  And ensure your python version matches.

---

# How To Use

Remove `uv run` prefix if `uv` unavailable.

- Apply migrations:
  ```
  uv run python ./src/django/manage.py migrate
  ```
- (Optional) Seed demo users and events:
  ```sh
  uv run python ./src/django/manage.py seed
  ```
- Run the server:
  ```sh
  uv run python ./src/django/manage.py runserver
  ```

---

# Demo Data & Credentials

Running `seed` (above) creates the following accounts:

| Role           | Username | Password          |
| -------------- | -------- | ----------------- |
| Superuser/admin| `admin`  | `cannybyte-admin` |
| Member         | `jess`   | `cannybyte-demo`  |
| Member         | `mo`     | `cannybyte-demo`  |

- The superuser can see the staff Dashboard to edit/delete any event.
- New members can also still signup.
