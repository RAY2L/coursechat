const express = require("express");
const app = express();
const ejs = require("ejs");
const path = require("path");

app.set("views", path.join(__dirname, "views"));
app.use(express.static(__dirname + "/public"));

app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("pages/index", { title: "Home" });
});

app.get("/:subject/:courseId", function (req, res) {
  const subject = req.params.subject;
  const courseId = req.params.courseId;

  const courses = ["CMSC 16100", "CMSC 23200", "CMSC 28000"];
  const course = `${subject} ${courseId}`;

  if (courses.includes(course)) {
    res.render("pages/course", { subject: subject, courseId: courseId });
  } else {
    res.redirect("/");
  }
});

// not `app.all(...)`?
app.get("*", (req, res) => {
  res.redirect("/");
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
