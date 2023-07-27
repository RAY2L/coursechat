const express = require("express");
const app = express();
const ejs = require("ejs");
const path = require("path");
const fs = require("fs");

app.set("views", path.join(__dirname, "views"));
// app.use(express.static(__dirname + "/public"));

app.set("view engine", "ejs");

const courses_raw_data = fs.readFileSync(
  path.join(__dirname, "data/courses.json")
);
const courses = JSON.parse(courses_raw_data);

const course_list = courses.map((course) => course["name"]);

const course_to_evalIDs_raw_data = fs.readFileSync(
  path.join(__dirname, "data/course_to_evalIDs.json")
);
const course_to_evalIDs = JSON.parse(course_to_evalIDs_raw_data);

const evalID_to_metadata_raw_data = fs.readFileSync(
  path.join(__dirname, "data/2022.json")
);
const evalID_to_metadata = JSON.parse(evalID_to_metadata_raw_data);

const course_to_metadatas = Object.fromEntries(
  Object.entries(course_to_evalIDs).map(([course, evalIDs]) => {
    // console.log(evalIDs);
    const metadatas = evalIDs.map((evalID) => {
      // console.log(evalID_to_metadata[evalID]);
      // console.log(evalID_to_metadata[evalID]);
      return evalID_to_metadata[evalID];
    });
    // console.log(course, metadatas);

    return [course, metadatas];
  })
);

// app.get("/eval/:evalID", (req, res) => {
//   const evalID = req.params.evalID;
//   // console.log(evalID);
//   const metadata = evalID_to_metadata[evalID];

//   res.render("pages/evaluation", { metadata: metadata });
// });

// app.get("/:subject/:courseId", function (req, res) {
//   const subject = req.params.subject;
//   const courseId = req.params.courseId;

//   // const courses = ["CMSC 16100", "CMSC 23200", "CMSC 28000"];
//   // console.log(course_to_evalIDs);
//   // console.log(evalID_to_metadata);
//   // console.log(course_to_metadatas);
//   const course = `${subject} ${courseId}`;

//   if (course_list.includes(course)) {
//     // console.log(course_to_evalIDs);
//     // console.log(course_to_metadatas[course]);
//     // console.log(course);
//     // console.log(course_to_metadatas[course]);
//     res.render("pages/course", {
//       subject: subject,
//       courseId: courseId,
//       evalIDs: JSON.stringify(course_to_evalIDs),
//       course_sections: course_to_metadatas[course],
//     });
//   } else {
//     res.redirect("/");
//   }
// });

// make sure to put this second to last...
app.get("/", (req, res) => {
  // console.log(courses);
  res.render("pages/index", { courses: JSON.stringify(courses) });
});

// not `app.all(...)`?
app.get("*", (req, res) => {
  res.redirect("/");
});

app.listen(process.env.PORT || 3000, () => {
  console.log("Server is running on port 3000");
});
