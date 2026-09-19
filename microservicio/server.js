require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { Pool } = require('pg');
const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const app = express();
app.use(cors());
app.use(express.json());

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

const swaggerSpec = swaggerJsdoc({
  definition: {
    openapi: '3.0.0',
    info: { title: 'Pokedex Microservicio', version: '1.0.0' }
  },
  apis: ['./server.js']
});
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));

app.get('/', async (req, res) => {
  try {
    await pool.query('SELECT 1');
    res.send('Conectado a la base de datos');
  } catch (err) {
    res.status(500).send('Error de conexión a la base de datos');
  }
});

/**
 * @swagger
 * /api/pokemones:
 *   get:
 *     summary: Lista todos los pokemones
 *     responses:
 *       200:
 *         description: Lista de pokemones
 */
app.get('/api/pokemones', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM pokemones');
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

/**
 * @swagger
 * /api/pokemones/{nombre}:
 *   get:
 *     summary: Busca un pokemon por nombre
 *     parameters:
 *       - in: path
 *         name: nombre
 *         required: true
 *         schema:
 *           type: string
 *     responses:
 *       200:
 *         description: Datos del pokemon
 *       404:
 *         description: No encontrado
 */
app.get('/api/pokemones/:nombre', async (req, res) => {
  try {
    const result = await pool.query(
      'SELECT * FROM pokemones WHERE nombre = $1',
      [req.params.nombre.toLowerCase()]
    );
    if (result.rows.length === 0) return res.status(404).json({ error: 'No encontrado' });
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Microservicio corriendo en puerto ${PORT}`));
