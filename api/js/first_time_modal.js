// When the DOM is ready
$(document).ready(function () {
  // Check if 'popupShown' is set in the localStorage
  if (!localStorage.getItem("popupShown")) {
    // If not set, then this is the first visit. Show the popup.
    $("#first_time_modal").modal("show");

    // Now set 'popupShown' in the localStorage so the popup will not appear again
    localStorage.setItem("popupShown", "true");
  }
});
