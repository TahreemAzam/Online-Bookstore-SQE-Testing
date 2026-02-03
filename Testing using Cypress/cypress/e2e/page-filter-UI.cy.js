describe('Shop Page Filters UI', () => {
    //TC: 03 --------Have Filer panels-------- 
  it('should display filter panels', () => {
    cy.get('h3').contains('Categories').should('be.visible');
    cy.get('h3').contains('Price range').should('be.visible');
    cy.get('h3').contains('Language').should('be.visible');
  });
  //TC: 04 -------Show Catagories Or not--------------
  it('should show category options', () => {
    cy.get('ul').contains('Biographies').should('exist');
    cy.get('ul').contains('Fiction').should('exist');
  });
});
