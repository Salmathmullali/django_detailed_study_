<h2>CRUD stands for the four basic operations you can perform on data in an application:</h2>

<li>C → Create → Add new data (e.g., a new user, task, or product).</li>

Example: INSERT in SQL, or creating a new object in Django (Model.objects.create(...)).

<li>R → Read → Retrieve or view existing data.</li>

Example: SELECT in SQL, or fetching data with Model.objects.all() in Django.

<li>U → Update → Modify existing data.</li>

Example: UPDATE in SQL, or editing a record in Django and calling .save().

<li>D → Delete → Remove data.</li>

Example: DELETE in SQL, or using .delete() in Django.<br>

In Django (and most web apps), CRUD refers to creating views and endpoints that let users:<br>

<li>Add a new record (C)</li>

<li>View/list records (R)</li>

<li>Edit a record (U)</li>

<li>Delete a record (D)</li><br>

<h3>A To-Do list app is a perfect example of CRUD:</h3>

<li>Create: Add a new task.</li>

<li>Read: Display the list of tasks.</li>

<li>Update: Mark a task as done or edit its text.</li>

<li>Delete: Remove a task.</li>
