The & concatenates the parent class, resulting in .title.sub-title (rather than .title .sub-title if the & is omitted).

The result is that with the & it matches an element with both title and sub-title classes:

<div class='title sub-title'></div> <!-- << match -->
whilst without the & it would match a descendent with class sub-title of an element with class title:

<div class='title'>
  ...
    <div class='sub-title'></div> <!-- << match -->
  ...
</div>