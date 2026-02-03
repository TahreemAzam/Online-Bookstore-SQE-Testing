describe('Taiga Login Test', () => {
  it('Should login successfully with local Docker Taiga', () => {
    cy.visit('http://localhost:9000/')

    cy.get('input[name="username"]').type('admin')
    cy.get('input[name="password"]').type('123123')
    cy.get('button:contains("Login")').click()

    cy.url().should('include', '/dashboard')
    cy.contains('Dashboard').should('be.visible')
  })
})
