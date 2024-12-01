#credit @codeflix_bots (telegram)

"""Get id of the replied user
Syntax: /id"""

from pyrogram import filters, enums
from pyrogram.types import Message

from bot import Bot


bot.command("pay", (ctx) => {
  return ctx.replyWithInvoice(
    "Test Product", // Product title
    "Test description", // Product description
    "{}", // Product payload, not required for now
    "XTR", // Stars Currency 
    [{ amount: 1, label: "Test Product" }, // Product variants
  ]);
});

bot.on("pre_checkout_query", (ctx) => {
  return ctx.answerPreCheckoutQuery(true).catch(() => {
    console.error("answerPreCheckoutQuery failed");
  });
});

// Map is used for simplicity. For production use a database
const paidUsers = new Map();

bot.on("message:successful_payment", (ctx) => {
  if (!ctx.message || !ctx.message.successful_payment || !ctx.from) {
    return;
  }

  paidUsers.set(
    ctx.from.id,
    ctx.message.successful_payment.telegram_payment_charge_id,
  );

  console.log(ctx.message.successful_payment);
});

bot.command("status", (ctx) => {
  const message = paidUsers.has(ctx.from.id)
    ? "You have paid"
    : "You have not paid yet";
  return ctx.reply(message);
});

bot.command("refund", (ctx) => {
  const userId = ctx.from.id;
  if (!paidUsers.has(userId)) {
    return ctx.reply("You have not paid yet, there is nothing to refund");
  }

  ctx.api
    .refundStarPayment(userId, paidUsers.get(userId))
    .then(() => {
      paidUsers.delete(userId);
      return ctx.reply("Refund successful");
    })
    .catch(() => ctx.reply("Refund failed"));
});

import express from "express";
import { Bot } from "grammy";

const app = express();
const port = 3000;

app.use(express.json());

const bot = new Bot(''); // Your bot token

app.post("/generate-invoice", async (req, res) => {
  const title = "Test Product";
  const description = "Test description";
  const payload = "{}";
  const currency = "XTR";
  const prices = [{ amount: 1, label: "Test Product" }];

  const invoiceLink = await bot.api.createInvoiceLink(
    title,
    description,
    payload,
    "", // Provider token must be empty for Telegram Stars
    currency,
    prices,
  );

  res.json({ invoiceLink });
});

// Call the endpoint we've just created
const response = await apiGetLink();

WebApp.openInvoice(response.invoiceLink, (status) => {
  if (status === "paid") {
    // Telegram notified us that the payment has been made
    // Refresh user's balance, plan, etc
  }
});
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
