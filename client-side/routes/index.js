const express = require('express')
const router = express.Router()
const logger = require('../public/javascript/middleware')
const rootProject = require('app-root-path')

router.use(logger)

const html_folder = rootProject.path + '/public/html/'

router.get('/', (req, res) => {
    res.sendFile(html_folder + 'index.html')
  })

router.use(express.static('public'))

module.exports = router;
