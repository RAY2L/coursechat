const express = require("express");
const app = express();
const ejs = require("ejs");
const path = require("path");
const fs = require("fs");

app.set("views", path.join(__dirname, "views"));
app.use(express.static("public"));
// app.use(express.static(__dirname + "/public"));

app.set("view engine", "ejs");

const current_courses_raw_data = fs.readFileSync(
  path.join(__dirname, "data/current_courses.json")
);
const current_courses = JSON.parse(current_courses_raw_data);

const courses_raw_data = fs.readFileSync(
  path.join(__dirname, "data/all_courses.json")
);
const courses = JSON.parse(courses_raw_data);

const course_list = courses.map((course) => course["name"]);

const course_to_evalIDs_raw_data = fs.readFileSync(
  path.join(__dirname, "data/course_to_evalIDs.json")
);
const course_to_evalIDs = JSON.parse(course_to_evalIDs_raw_data);

const evalID_to_metadata_raw_data = fs.readFileSync(
  path.join(__dirname, "data/combine_years.json")
);
const evalID_to_metadata = JSON.parse(evalID_to_metadata_raw_data);

const current_course_to_coursename_raw_data = fs.readFileSync(
  path.join(__dirname, "data/current_course_to_coursename.json")
);
const current_course_to_coursename = JSON.parse(
  current_course_to_coursename_raw_data
);

const all_course_to_coursename_raw_data = fs.readFileSync(
  path.join(__dirname, "data/all_course_to_coursename.json")
);
const all_course_to_coursename = JSON.parse(all_course_to_coursename_raw_data);

const current_course_to_IDs_raw_data = fs.readFileSync(
  path.join(__dirname, "data/current_course_to_IDs.json")
);
const current_course_to_IDs = JSON.parse(current_course_to_IDs_raw_data);

const current_ID_to_metadatas_raw_data = fs.readFileSync(
  path.join(__dirname, "data/cur.json")
);
const current_ID_to_metadatas = JSON.parse(current_ID_to_metadatas_raw_data);

const summaries_raw_data = fs.readFileSync(
  path.join(__dirname, "data/summaries.json")
);
const summaries = JSON.parse(summaries_raw_data);

// sort alphabetically here (instead of at route level)
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

const current_course_to_metadatas = Object.fromEntries(
  Object.entries(current_course_to_IDs).map(([course, IDs]) => {
    // console.log(IDs);
    const metadatas = IDs.map((ID) => {
      // console.log(ID_to_metadata[ID]);
      // console.log(ID_to_metadata[ID]);
      return current_ID_to_metadatas[ID];
    });
    // console.log(course, metadatas);

    return [course, metadatas];
  })
);

app.get("/current_section/:current_section_ID", (req, res) => {
  const current_section_ID = req.params.current_section_ID;
  // console.log(current_section_ID);
  const metadata = current_ID_to_metadatas[current_section_ID];

  res.render("pages/current_course_section", { metadata: metadata });
});

app.get("/eval/:evalID", (req, res) => {
  const evalID = req.params.evalID;
  // console.log(evalID);
  const metadata = evalID_to_metadata[evalID];
  // console.log(metadata["Catalog Number"]);
  // console.log(metadata["Catalog Number"][0]["Subject"]);
  const summary = summaries[evalID]?.["Summary"];
  // console.log(summary);

  res.render("pages/evaluation", { metadata: metadata, summary: summary });
});

app.get("/:subject/:courseId", function (req, res) {
  const subject = req.params.subject;
  const courseId = req.params.courseId;

  // const courses = ["CMSC 16100", "CMSC 23200", "CMSC 28000"];
  // console.log(course_to_evalIDs);
  // console.log(evalID_to_metadata);
  // console.log(course_to_metadatas);
  const course = `${subject} ${courseId}`;

  if (course_list.includes(course)) {
    // console.log(course_to_evalIDs);
    // console.log(course_to_metadatas[course]);
    // console.log(course);
    // console.log(course_to_metadatas[course]);
    const current_course_sections = current_course_to_metadatas[course] || [];
    const course_sections = course_to_metadatas[course] || [];

    current_course_sections.sort((course_1, course_2) => {
      if (course_1["Instructors"][0] < course_2["Instructors"][0]) {
        return -1;
      }
      if (course_1["Instructors"][0] > course_2["Instructors"][0]) {
        return 1;
      }
      return 0;
    });

    course_sections.sort((course_1, course_2) => {
      if (course_1["Instructors"][0] < course_2["Instructors"][0]) {
        return -1;
      }
      if (course_1["Instructors"][0] > course_2["Instructors"][0]) {
        return 1;
      }
      return 0;
    });

    res.render("pages/course", {
      subject: subject,
      courseId: courseId,
      // evalIDs: JSON.stringify(course_to_evalIDs),
      current_course_sections: current_course_sections,
      course_sections: course_sections,
      course_name: all_course_to_coursename[course],
    });
  } else {
    res.redirect("/");
  }
});

app.get("/info", (req, res) => {
  // console.log(courses);
  res.render("pages/info");
});

// make sure to put this second to last...
app.get("/", (req, res) => {
  // console.log(courses);
  res.render("pages/index", {
    current_courses: JSON.stringify(current_courses),
    courses: JSON.stringify(courses),
    current_course_to_coursename: JSON.stringify(current_course_to_coursename),
    all_course_to_coursename: JSON.stringify(all_course_to_coursename),
  });
});

// not `app.all(...)`?
app.get("*", (req, res) => {
  res.redirect("/");
});

app.listen(process.env.PORT || 3000, () => {
  console.log("Server is running on port 3000");
});
