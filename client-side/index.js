const express = require('express')
const main = require('./routes/index')

const app = express()
const port = 3000

app.use('/', main)

app.listen(port, () => console.log(`app listening on port ${port}!`))
