const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    defaultCommandTimeout: 20000,  // 20 seconds
    pageLoadTimeout: 60000,        // 60 seconds
    responseTimeout: 60000,        // 60 seconds
    requestTimeout: 60000,          // 60 seconds
    screenshotOnRunFailure: true,
    video: false,       // optional: disable video recording
  },
  env: {
    screenshotOnPass: true
  }
});
