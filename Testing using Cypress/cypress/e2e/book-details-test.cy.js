describe('TC-15 - Click on book and navigate to details page', () => {

  beforeEach(() => {
    cy.visit('https://sahup9156.github.io/bookworms/shop.html');
  });

  it('TC-15 - Clicking on a book opens a new page', () => {

    // Click first valid link inside the shop page (book image/title)
    cy.get('a[href]')
      .filter((index, el) => {
        const href = el.getAttribute('href');
        return (
          href &&
          !href.includes('#') &&
          !href.includes('shop.html') &&
          !href.includes('index.html')
        );
      })
      .first()
      .should('be.visible')
      .click();

    // Validate navigation to new page
    cy.url().should('not.include', 'shop.html');

    // Validate that some book details are visible on new page
    cy.get('h1, h2, h3, h4')
      .first()
      .should('be.visible');

    // Screenshot evidence
    cy.screenshot('TC-15-Book-Details-Page');
  });

});
