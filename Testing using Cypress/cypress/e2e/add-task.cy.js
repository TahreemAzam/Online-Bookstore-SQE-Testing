describe('Taiga Add Task Test', () => {
  it('Should add a new task (User Story) in the project', () => {
    cy.visit('https://app.taiga.io/') // Or local Taiga URL

    // Login first
    cy.get('input[name="username"]').type('your_email')
    cy.get('input[name="password"]').type('your_password')
    cy.get('button:contains("Login")').click()
    cy.wait(3000)

    // Open project
    cy.contains('Test Project').click()
    cy.wait(3000)

    // Add a User Story / Task
    cy.contains('User Stories').click()
    cy.contains('Add User Story').click()
    cy.get('input[name="subject"]').type('Test Task')
    cy.contains('Save').click()
    
    // Verify task added
    cy.contains('Test Task').should('be.visible')
  })
})