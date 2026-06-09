# Test Plan

## T01: Site looks professional and works on phones

- **Description:** Check that every page has the same menu bar and layout, and still looks right on a small screen.
- **Input:** Open the home page, the events page, and an event page, then make the browser window narrow.
- **Expected result:** Every page has the same styled menu and layout, and the content stacks on a small screen.
- **Actual result:** Pass
- **Actions taken:** When I first opened the site, one page showed an error due to how the `django-components` package works, I found the issue and fixed it after reading the documentation.

## T02: Sign up with correct details

- **Description:** A new visitor can create an account.
- **Input:** Go to the Sign up page, enter a new username, an email, and the same password twice, then click Sign up.
- **Expected result:** The account is created, the visitor is logged in automatically, and is taken to the events page.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T03: Sign up with passwords that do not match

- **Description:** The two password boxes must match.
- **Input:** On the Sign up page, type one password in the first box and a different one in the second, then click Sign up.
- **Expected result:** A message says the passwords do not match, and no account is created.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T04: Sign up with a username already taken

- **Description:** Two people cannot share the same username.
- **Input:** On the Sign up page, try to sign up using a username that already exists, such as jess.
- **Expected result:** A message says the username is taken, and no account is created.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T05: Log in with correct details

- **Description:** A member can log in and reach the members area.
- **Input:** Go to the Log in page, enter a valid username and password, such as jess, then click Log in.
- **Expected result:** The member is taken to the events page, and the menu now shows their name, a New event button, and Log out.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T06: Log in with the wrong password

- **Description:** Wrong details are refused.
- **Input:** On the Log in page, enter a valid username with an incorrect password.
- **Expected result:** A message says the details are incorrect, and the person stays logged out.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T07: Members pages are private

- **Description:** People who are not logged in cannot see the members pages.
- **Input:** While logged out, try to open the events page, an event page, the My events page, and the New event page.
- **Expected result:** Each time, the person is sent to the Log in page instead of seeing the content.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T08: Log out

- **Description:** A logged in member can log out.
- **Input:** While logged in, click Log out in the menu.
- **Expected result:** The member is logged out, a confirmation page is shown, and the members pages can no longer be opened.
- **Actual result:** Pass
- **Actions taken:** At first the Log out option showed an error. I changed how the Log out button works by submitting a post form (what django expects), and it now logs the member out successfully.

## T09: See all events

- **Description:** Logged in members can see every event on the site.
- **Input:** Log in and open the events page.
- **Expected result:** All events are shown as cards with their title, date, and location.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T10: Search events by title

- **Description:** Members can find events by typing part of the title.
- **Input:** On the events page, type "food" in the Search by title box and click Filter.
- **Expected result:** Only events whose title contains "food" are shown, such as the Community Food Bank.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T11: Search with no results

- **Description:** A search that matches nothing does not cause an error.
- **Input:** On the events page, search for something that does not exist.
- **Expected result:** No events are shown, with a message saying none were found, and no error.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T12: Filter events by date

- **Description:** Members can see events on a chosen date.
- **Input:** On the events page, choose the date 18 June 2026 and click Filter.
- **Expected result:** Only the event on that date is shown, such as the Budgeting Workshop.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T13: A bad date does not break the page

- **Description:** Typing something that is not a real date must not cause an error.
- **Input:** On the events page, enter an invalid date.
- **Expected result:** The date filter is ignored, all events are shown, and there is no error.
- **Actual result:** Pass
- **Actions taken:** I made sure that an entry which is not a real date shows all events instead of causing an error.

## T14: Create an event with a picture

- **Description:** A member can add a new event, including a picture.
- **Input:** Go to New event, fill in the title, date, time, location, and description, choose a picture, then click Publish.
- **Expected result:** The event is saved under the member's name, the picture is shown, and the new event page opens.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T15: Create an event with missing details

- **Description:** Important boxes must be filled in.
- **Input:** On the New event page, leave the title and date empty and click Publish.
- **Expected result:** The page shows which boxes are required, and no event is created.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T16: Edit your own event

- **Description:** A member can change an event they created.
- **Input:** Log in as the owner, open one of their events, click Edit, change the title, and click Save.
- **Expected result:** The form is already filled in, the change is saved, and the updated event is shown.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T17: Delete your own event with confirmation

- **Description:** Deleting always asks for confirmation first.
- **Input:** Open one of your own events, click Delete, then confirm on the next page.
- **Expected result:** A confirmation page appears first, and only after confirming is the event removed.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T18: You cannot change someone else's event

- **Description:** A member cannot edit or delete another member's event.
- **Input:** While logged in as mo, try to open the edit page for an event owned by jess.
- **Expected result:** The action is blocked, the event is unchanged, and the Edit and Delete buttons are not shown to people who do not own the event.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T19: Only admins can open the admin dashboard

- **Description:** The admin dashboard is for staff only.
- **Input:** Try to open the admin dashboard first as an ordinary member, then as the admin.
- **Expected result:** The ordinary member is sent to the Log in page, while the admin sees the dashboard listing all events and their owners.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T20: Admin can change any event

- **Description:** An administrator can edit or delete events created by other people.
- **Input:** Log in as the admin and, from the dashboard, edit and then delete an event owned by another member.
- **Expected result:** The admin can edit and delete the event even though they did not create it.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T21: Leave a comment

- **Description:** Any logged in member can comment on an event.
- **Input:** Log in, open an event, type a comment, and click Post.
- **Expected result:** The comment is saved, appears in the list on the event, and the comment count goes up.
- **Actual result:** Pass
- **Actions taken:** None needed.

## T22: Empty comments are not posted

- **Description:** A blank comment cannot be posted.
- **Input:** On an event page, click Post without typing anything.
- **Expected result:** Nothing is posted, and the comment box asks for some text.
- **Actual result:** Pass
- **Actions taken:** None needed.
