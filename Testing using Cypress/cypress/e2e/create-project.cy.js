describe('Taiga Create Project Test', () => {
  it('Should create a new project successfully', () => {
    cy.visit('https://app.taiga.io/') // Or local Taiga URL

    // Login first
    cy.get('input[name="username"]').type('your_email')
    cy.get('input[name="password"]').type('your_password')
    cy.get('button:contains("Login")').click()
    cy.wait(3000)

    // Click New Project
    cy.contains('New Project').click()
    cy.get('input[name="name"]').type('Test Project') // Project name
    cy.contains('Create').click()
    
    // Verify project created
    cy.contains('Test Project').should('be.visible')
  })
})
