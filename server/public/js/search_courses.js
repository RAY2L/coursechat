$("#autocomplete-input")
  .typeahead({
    source: courses,
    autoSelect: true,
    displayText: function (item) {
      return item.name;
    },
    afterSelect: function (item) {
      window.location.href =
        "/" + item.value.subject + "/" + item.value.courseId;
    },
  })
  .keypress(function (e) {
    if (e.which == 13) {
      const inputVal = $(this).val();
      const uniqueMatch = courses.filter(function (choice) {
        return choice.name.toLowerCase() === inputVal.toLowerCase();
      });
      if (uniqueMatch.length === 1) {
        window.location.href =
          "/" +
          uniqueMatch[0].value.subject +
          "/" +
          uniqueMatch[0].value.courseId;
      }
    }
  });
